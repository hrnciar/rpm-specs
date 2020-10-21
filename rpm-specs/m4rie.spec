Name:           m4rie
Version:        20200125
Release:        3%{?dist}
Summary:        Linear Algebra over F_2^e
License:        GPLv2+
URL:            https://bitbucket.org/malb/%{name}
Source0:        https://bitbucket.org/malb/%{name}/downloads/%{name}-%{version}.tar.gz
# Fix compiler warnings that may indicate runtime / test-time problems
Patch0:         %{name}-warning.patch
# Remove unnecessary direct library dependencies from the pkgconfig file,
# and also cflags used to compile m4rie, but not needed by consumers of m4rie.
Patch1:         %{name}-pkgconfig.patch

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(m4ri)

%description
M4RIE is a library for fast arithmetic with dense matrices over F_2^e.
It is an add-on to the M4RI library, which implements fast arithmetic
with dense matrices over F_2.  M4RIE is used by the Sage mathematics
software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       m4ri-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static %{name} library.

%prep
%autosetup -p0

%build
%configure

# Die, rpath, die!  Also workaround libtool reordering -Wl,--as-needed after
# all the libraries
sed -e "s|\(hardcode_libdir_flag_spec=\)'.*|\1|" \
    -e "s|\(runpath_var=\)LD_RUN_PATH|\1|" \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
cd m4rie
doxygen
cd -

%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%check
make check

%files
%license COPYING
%{_libdir}/lib%{name}-0.0.%{version}.so

%files devel
%doc doc/html
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files static
%{_libdir}/lib%{name}.a

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Jerry James <loganjerry@gmail.com> - 20200125-1
- Version 20200125

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 20200115-1
- Version 20200115
- Add -pkgconfig patch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150908-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 20150908-1
- New upstream release
- Drop unneeded givaro-devel BR
- Update URLs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140914-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Jerry James <loganjerry@gmail.com> - 20140914-2
- Add LaTeX BR to fix FTBFS (see bz 1198355)
- Drop workaround for m4ri pkgconfig bug now that m4ri is fixed

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 20140914-1
- New upstream release
- Drop upstreamed -aarch64 and -doxygen patches
- Fix license handling

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May  9 2013 Jerry James <loganjerry@gmail.com> - 20130416-2
- Bump and rebuild to fix bad F19 build

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 20130416-1
- New upstream release
- Add -aarch64 and -doxygen patches
- Build PDF documentation instead of HTML, because of numerous TeX-only
  constructs in the documentation

* Fri Feb  8 2013 Jerry James <loganjerry@gmail.com> - 20120613-3
- Rebuild for givaro 3.7.2

* Mon Dec 31 2012 Jerry James <loganjerry@gmail.com> - 20120613-2
- Rebuild for m4ri 20121224

* Mon Dec 10 2012 Jerry James <loganjerry@gmail.com> - 20120613-1
- New upstream release

* Tue Oct  2 2012 Jerry James <loganjerry@gmail.com> - 20120415-4
- Rebuild for givaro 3.7.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120415-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Jerry James <loganjerry@gmail.com> - 20120415-2
- Fix -static Requires

* Wed Apr 25 2012 Jerry James <loganjerry@gmail.com> - 20120415-1
- Initial RPM
