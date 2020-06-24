Name:		xxhash
Version:	0.7.3
Release:	1%{?dist}
Summary:	Extremely fast hash algorithm

#		The source for the library (xxhash.c and xxhash.h) is BSD
#		The source for the command line tool (xxhsum.c) is GPLv2+
License:	BSD and GPLv2+
URL:		http://www.xxhash.com/
Source0:	https://github.com/Cyan4973/xxHash/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc

%description
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package libs
Summary:	Extremely fast hash algorithm - library
License:	BSD

%description libs
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package devel
Summary:	Extremely fast hash algorithm - development files
License:	BSD
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for the xxhash library

%prep
%setup -q -n xxHash-%{version}

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" MOREFLAGS="%{?__global_ldflags} -fPIC"

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm %{buildroot}/%{_libdir}/libxxhash.a

%check
make check
make test-xxhsum-c

%ldconfig_scriptlets libs

%files
%{_bindir}/xxh*sum
%{_mandir}/man1/xxh*sum.1*
%license LICENSE
%doc README.md

%files libs
%{_libdir}/libxxhash.so.*
%license LICENSE
%doc README.md

%files devel
%{_includedir}/xxhash.h
%{_includedir}/xxh3.h
%{_libdir}/libxxhash.so
%{_libdir}/pkgconfig/libxxhash.pc

%changelog
* Fri Mar 06 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.7.3-1
- Update to version 0.7.3
- Drop patch xxhash-gcc10-altivec.patch (accepted upstream)

* Fri Feb 07 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.7.2-3
- Fix ppc64le build with gcc 10

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.7.2-1
- Update to version 0.7.2

* Sat Aug 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.7.1-1
- Update to version 0.7.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.7.0-1
- Update to version 0.7.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.5-1
- Update to version 0.6.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.4-1
- Update to version 0.6.4
- Drop previously backported patches

* Thu Oct 19 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.3-2
- Correct License tag (command line tool is GPLv2+)
- Adjust Source tag to get a more descriptive tarfile name

* Wed Oct 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.3-1
- Initial packaging
