Name:           pynac
Version:        0.7.26
Release:        2%{?dist}
Summary:        Manipulation of symbolic expressions
License:        GPLv2+
URL:            http://pynac.org/
Source0:        https://github.com/pynac/pynac/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
# Remove pessimizing calls to std::move
Patch0:         %{name}-pessimizing-move.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  flint-devel
BuildRequires:  giac-devel
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(factory)
BuildRequires:  python3-devel


%description
Pynac is a derivative of the C++ library GiNaC, which allows manipulation of
symbolic expressions. It currently provides the backend for symbolic
expressions in Sage.

The main difference between Pynac and GiNaC is that Pynac relies on Sage to
provide the operations on numerical types, while GiNaC depends on CLN for this
purpose.


%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
Headers and libraries for developing with %{name}.


%prep
%autosetup -p0

# GCC 8 does not support this warning
sed -i 's/ -Wno-parentheses-equality//' ginac/Makefile.in

%build
export PYTHON=%{__python3}
%configure --disable-static --disable-silent-rules

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib%{name}.so.*


%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.26-2
- Rebuilt for Python 3.9

* Mon Feb 24 2020 Jerry James <loganjerry@gmail.com> - 0.7.26-1
- Update to 0.7.26 for sagemath 8.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 0.7.24-6
- Rebuild for ntl 11.4.3

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 0.7.24-5
- Rebuild for mpfr 4

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 0.7.24-4
- Rebuild for ntl 11.3.4

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.24-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 0.7.24-1
- Update to 0.7.24 for sagemath 8.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Jerry James <loganjerry@gmail.com> - 0.7.22-3
- Rebuild for Singular 4.1.1p3

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 0.7.22-2
- Rebuild for ntl 11.3.0
- Build for python 3 instead of python 2

* Sat Sep 22 2018 Jerry James <loganjerry@gmail.com> - 0.7.22-1
- Update to 0.7.22 for sagemath 8.3

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 0.7.16-4
- Rebuild for ntl 11.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 0.7.16-2
- Rebuild for ntl 11.1.0

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 0.7.16-1
- Update to 0.7.16 required by newer sagemath
- Giac is now available on all arches
- Use ldconfig macro

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.7.8-1
- Update to 0.7.8 required by newer sagemath

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 0.7.5-4
- Build with giac support on supported architectures
- Add --disable-silent-rules to configure invocation
- Explicitly use python 2 until we are ready to switch to python 3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.7.5-1
- Update to 0.7.5 required by newer sagemath

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Mar 29 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.7.3=1
- Update to 0.7.3 required by newer sagemath

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.6.9-1
- Update to 0.6.9, required by newer sagemath

* Wed Aug 10 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.6.7-1
- Update to 0.6.7, required by newer sagemath

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.3.9.2-1
- Update to 0.3.9.2, required by newer sagemath

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Apr  3 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.3.2-5
- Rebuild for new c++ string and list abi

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.3.2-2
- Update metadata and rebuild.

* Mon May 26 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.3.2-1
- Update to latest upstream release.

* Sat Sep 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.3.0-1
- Update to latest upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.2.5-1
- Update to latest upstream release.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.2.4-1
- Update to latest upstream release.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.2.3-1
- update to new version (#731321)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec  7 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.2.1-1
- update to new version
- fix ftbfs #631289

* Wed Jan 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.11-1
- update to new version
- use {buildroot} and {optflags}
- install preserving timestamps
- R: pkgconfig

* Fri Jan 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.10-1
- update to new version
- use %%global and not %%define

* Fri Oct 16 2009 Thomas Spura <tomspur@fedoraproject.org> - 0.1.9-2
- disable static librariy

* Sun Oct 11 2009 Thomas Spura <tomspur@fedoraproject.org> - 0.1.9-1
- Bumped to new version 0.1.9
- description modified

* Sat Mar 21 2009 Conrad Meyer <konrad@tylerc.org> - 0.1.3-1
- Initial package.
