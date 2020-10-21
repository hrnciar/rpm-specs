Name:           ustl
Version:        2.8
Release:        5%{?dist}
Summary:        A size-optimized STL implementation
License:        MIT
URL:            http://msharov.github.io/ustl/
Source0:        https://github.com/msharov/ustl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-static
BuildRequires:  pkgconfig
BuildRequires:  make
BuildRequires:  sed

%description
The C++ standard template library (STL) is a collection of common containers 
and algorithms in template form. Unfortunately its standard incarnation 
shipped with gcc is implemented without much concern for code size. Not only 
is the library itself large, the current version being over a megabyte in 
size, but with all the code you instantiate by using a vector for each of 
your containers, it is easy to become fearful and opt for using static 
arrays instead or, worse yet, abandon C++ altogether for C. This is 
especially painful to former DOS assembly programmers like myself, who fret 
endlessly when the size of the executable crosses the magic 64k boundary, 
forgetting that nobody cares about memory anymore.

Of course, these days everyone has gigabytes of RAM and has no compunction 
about loading up OpenOffice, whose source tree is over a gigabyte in size. 
Why then bother with saving a kilobyte of code here and there? I can't really 
say. Maybe it's that warm fuzzy knowledge that you are making maximum possible
use of your computer's resources. Maybe it's that thrill you get after 
expressing your program's functionality in the fewest possible instructions 
and the minimum imaginable overhead. Or maybe it really is of no importance 
and any code bloat will be easily overcome by faster processors in some near 
future. I just know what I like, and it's the sight of clean, concise, and 
fast code. Therefore this library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

# No silent build.
sed -i -e 's|\t@|\t|g' Makefile

# Don't strip the symbols, substituted with correct ldflags.
sed -i -e 's|/usr/lib|%{_libdir}|g'  \
    -i -e 's|-s |%{?__global_ldflags} |g'  \
       -e 's|CXXFLAGS	:=|override CXXFLAGS	+=|g' \
   Config.mk.in

# Do not interfere with optflags
sed -i -e 's|-march=native||g' configure

# Fix pkgconfig file
sed -i '/^prefix=/d' ustl.pc.in
sed -i -e 's|${prefix}/lib|%{_libdir}|g' ustl.pc.in
sed -i -e 's|${prefix}/include|%{_includedir}|g' ustl.pc.in

%build
./configure \
  --prefix=%{buildroot}%{_prefix} \
%ifarch %{ix86}
  --without-mmx \
%endif
  --with-libstdc++ --force-inline

%make_build CXXFLAGS+="%{optflags}"

%install
%make_install LIBDIR="%{buildroot}%{_libdir}" PKGCONFIGDIR="%{buildroot}%{_libdir}/pkgconfig"

chmod 755 -v %{buildroot}%{_libdir}/*

%check
make check

%ldconfig_scriptlets

%files
%license LICENSE
%doc README
%{_libdir}/libustl.so.*

%files devel
%doc docs/*
%{_includedir}/ustl.h
%{_includedir}/ustl/
%{_libdir}/libustl.so
%{_libdir}/pkgconfig/ustl.pc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Denis Fateyev <denis@fateyev.com> - 2.8-1
- Update to 2.8 version

* Thu Aug 02 2018 Denis Fateyev <denis@fateyev.com> - 2.7-1
- Update to 2.7 version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Denis Fateyev <denis@fateyev.com> - 2.5-1
- Update to 2.5 version

* Fri May 20 2016 Denis Fateyev <denis@fateyev.com> - 2.4-1
- Update to 2.4 version
- Dropping obsolete patches

* Mon Feb 29 2016 Denis Fateyev <denis@fateyev.com> - 2.3-1
- Update to 2.3 version (including patches)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.1-3
- Remove -march=native
- Disable SSE on ix86 (not supported by default optflags)

* Tue Jul 29 2014 Christopher Meng <rpm@cicku.me> - 2.1-2
- Fix library location on lib64 system.

* Tue Jan 21 2014 Christopher Meng <rpm@cicku.me> - 2.1-1
- Initial Package.
