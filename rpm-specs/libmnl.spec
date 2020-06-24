Name:          libmnl
Version:       1.0.4
Release:       11%{?dist}
Summary:       A minimalistic Netlink library

License:       LGPLv2+
URL:           http://netfilter.org/projects/libmnl
Source0:       http://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2

BuildRequires: gcc

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use code and
to avoid re-inventing the wheel.


%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}

%package       static
Summary:       Static development files for %{name}
Requires: %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description 	static
The %{name}-static package contains static libraries for devleoping applications that use %{name}.


%prep
%setup -q


%build
%configure --enable-static
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete
find examples '(' -name 'Makefile.am' -o -name 'Makefile.in' ')' -delete
find examples -type d -name '.deps' -prune -exec rm -rf {} ';'
mv examples examples-%{_arch}


%ldconfig_scriptlets


%files
%license COPYING
%doc README
%{_libdir}/*.so.*

%files devel
%doc examples-%{_arch}
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files static
%{_libdir}/*.a

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.4-1
- Add gcc BuildReq, cleanup spec

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Hushan Jia <hushan.jia@gmail.com> 1.0.4-1
- Update to 1.0.4.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.3-8
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 12 2012 Hushan Jia <hushan.jia@gmail.com> - 1.0.3-4
- use %%doc for each arch to avoid multilib conflict (rhbz 831413)

* Sat Aug 04 2012 Philip Prindeville <philipp@fedoraproject.org> - 1.0.3-3
- Add .a to devel package (rhbz 845793)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Hushan Jia <hushan.jia@gmail.com> 1.0.3-1
- Update to 1.0.3.

* Sat Feb 04 2012 Hushan Jia <hushan.jia@gmail.com> 1.0.2-1
- Update to 1.0.2.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 24 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-4
- fix require of devel package
- add example source files to docs

* Wed Aug 24 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-3
- remove unnecessary buildroot and defattr tags
- remove unnecessary build requires

* Sat Aug 20 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-2
- use upstream released source tarball

* Sat Aug 20 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-1
- initial packaging

