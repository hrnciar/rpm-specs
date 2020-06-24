%global		module		Bcp

Name:		coin-or-%{module}
Summary:	Branch-Cut-Price Framework
Version:	1.4.4
Release:	3%{?dist}
License:	CPL
URL:		http://projects.coin-or.org/%{module}
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
BuildRequires:	coin-or-Cgl-devel
BuildRequires:	coin-or-Cgl-doc
BuildRequires:	coin-or-Clp-doc
BuildRequires:	coin-or-Vol-devel
BuildRequires:	coin-or-Vol-doc
BuildRequires:	doxygen
BuildRequires:	gcc-c++

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

%description
BCP is a parallel framework for implementing branch, cut, and price algorithms
for solving mixed integer programs (MIPs). BCP provides the user with an
object-oriented framework that can be used to develop an efficient problem
class specific MIP solver without all the implementational effort. involved
with implementing a branch and bound framework from scratch.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Osi-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Cgl-doc
Requires:	coin-or-Clp-doc
Requires:	coin-or-Vol-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description    doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,bcp_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%ldconfig_scriptlets

%files
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/README
%{_libdir}/libBcp.so.1
%{_libdir}/libBcp.so.1.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libBcp.so
%{_libdir}/pkgconfig/bcp.pc

%files          doc
%{_pkgdocdir}/html/
%{_pkgdocdir}/bcp_doxy.tag

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.4.4-1
- Update to latest upstream release
- Eliminate unnecessary BRs and Rs
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files
- Add -doc subpackage; run doxygen

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.4.3-8
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.4.3-1
- Update to latest upstream release
- Remove no longer needed pkgconfig patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.8-7
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.8-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.8-4
- Rebuild to ensure using latest C++ abi changes.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.8-1
- Update to latest upstream release.

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.6-2
- Use proper _smp_flags macro (#894586#c6).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.6-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.4-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.4-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.4-2
- Rename package to coin-or-Bcp.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.4-1
- Initial coinor-Bcp spec.
