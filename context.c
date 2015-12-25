#include <malloc.h>
#include <ucontext.h>
#include <stdio.h>

// 64kB stack
#define FIBER_STACK 1024*64

ucontext_t child, parent;

// The child thread will execute this function
void threadFunction()
{
         printf( "Child fiber yielding to parent" );
         swapcontext( &child, &parent );
         printf( "Child thread exiting\n" );
         swapcontext( &child, &parent );
}

int main()
{
         // Get the current execution context
         getcontext( &child );

         // Modify the context to a new stack
         child.uc_link = 0; //This is a pointer to the next context structure which is used if the context described in the current structure returns
         child.uc_stack.ss_sp = malloc( FIBER_STACK ); //stack pointer
         child.uc_stack.ss_size = FIBER_STACK; //stack size
         child.uc_stack.ss_flags = 0; // ?
         if ( child.uc_stack.ss_sp == 0 )
         {
                 perror( "malloc: Could not allocate stack" );
                 exit( 1 );
         }

         // Create the new context
         printf( "Creating child fiber\n" );
         makecontext( &child, &threadFunction, 0 ); // last variable is argument to the function
        
         // Execute the child context
         printf( "Switching to child fiber\n" );
         swapcontext( &parent, &child );
         printf( "Switching to child fiber again\n" );
         swapcontext( &parent, &child );

         // Free the stack
         free( child.uc_stack.ss_sp );

         printf( "Child fiber returned and stack freed\n" );
        
         return 0;
}