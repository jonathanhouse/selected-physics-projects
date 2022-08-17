module fourier

    implicit none
    private
    public fft

        contains

        function fft(x) result(e_curr)
            
            real,intent(in) :: x(:)
            complex,allocatable :: e_curr(:),e_prev(:)
            integer :: N,m,j,k,s,b,levels
            complex,parameter :: i = (0,1)
            real,parameter :: pi = 3.14159
            N = size(x)
            levels = nint( log(real(N))/log(2.) )
            allocate(e_curr(0:N-1))
            allocate(e_prev(0:N-1))
            e_prev(:) = [(complex(x(b),0), b = 1,N,1)]
            !print *,e_prev
            loop_m: do m = levels-1,0,-1
                loop_j: do j = 0,(2**m)-1
                    loop_k: do k = 0,(N/(2**m))-1
                        s = k
                        if (k > N/(2**(m+1)) - 1) then 
                            s = s - N/(2**(m+1))
                        end if 
                        e_curr(j+k*2**m) = e_prev(j+s*(2**(m+1))) + cexp(-i*2*pi*(2**m)*k/N)*e_prev(j+s*2**(m+1)+2**m)
                    end do loop_k
                end do loop_j
                e_prev(:) = e_curr(:)
            end do loop_m
            deallocate(e_prev)

    end function fft

end module fourier


program main

    use fourier
    implicit none

    integer,parameter :: n = 1024
    real,dimension(0:n-1) :: pitches 
    real,dimension(0:n-1) :: c
    real,dimension(0:n-1) :: t
    integer :: i

    ! inserts pitch.txt data into array pitches
    open(unit=10,file='pitch.txt',action='read',status='old')
    do i = 0,n-1
        read(10,*) pitches(i)
    end do

    t = [(i,i=0,n-1)]
    c = abs(fft(pitches))

    do i = 0,n/2-1
    print '(2(f15.8))', t(i),c(i)
    end do

end program main
