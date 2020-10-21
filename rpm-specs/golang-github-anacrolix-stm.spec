# Generated by go2rpm 1
%bcond_without check

# https://github.com/anacrolix/stm
%global goipath         github.com/anacrolix/stm
Version:                0.2.0

%gometa

%global common_description %{expand:
Package stm provides Software Transactional Memory operations for Go. This is an
alternative to the standard way of writing concurrent code (channels and
mutexes). STM makes it easy to perform arbitrarily complex operations in an
atomic fashion. One of its primary advantages over traditional locking is that
STM transactions are composable, whereas locking functions are not -- the
composition will either deadlock or release the lock between functions (making
it non-atomic).

The stm API tries to mimic that of Haskell's Control.Concurrent.STM, but this is
not entirely possible due to Go's type system; we are forced to use interface{}
and type assertions. Furthermore, Haskell can enforce at compile time that STM
variables are not modified outside the STM monad. This is not possible in Go, so
be especially careful when using pointers in your STM code. Another significant
departure is that stm.Atomically does not return a value. This shortens
transaction code a bit, but I'm not 100% it's the right decision. (The
alternative would be for every transaction function to return an interface{}.)}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Software Transactional Memory in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/anacrolix/missinggo/iter)
BuildRequires:  golang(github.com/benbjohnson/immutable)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/anacrolix/envpprof)
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|github.com/anacrolix/missinggo/v2|github.com/anacrolix/missinggo|" "{}" +;

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jan 26 23:25:53 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package