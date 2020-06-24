Name:		castxml
Version:	0.3.1
Release:	1%{?dist}
Summary:	C-family abstract syntax tree XML output tool

License:	ASL 2.0
URL:		https://github.com/CastXML/CastXML
Source0:	https://github.com/CastXML/CastXML/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	llvm-devel >= 3.6.0
BuildRequires:	clang-devel >= 3.6.0
BuildRequires:	libedit-devel
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/sphinx-build
Obsoletes:	gccxml < 0.9.0-0.28

%description
Parse C-family source files and optionally write a subset of the
Abstract Syntax Tree (AST) to a representation in XML.

Source files are parsed as complete translation units using the clang
compiler. XML output is enabled by the --castxml-gccxml option and
produces a format close to that of gccxml. Future versions of castxml
may support alternative output formats.

%prep
%setup -q -n CastXML-%{version}

%build
%cmake -DCastXML_INSTALL_DOC_DIR:STRING=share/doc/%{name} \
       -DCastXML_INSTALL_MAN_DIR:STRING=share/man \
       -DCLANG_RESOURCE_DIR:PATH=$(clang -print-file-name=include)/.. \
       -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
%if %{?fedora}%{!?fedora:0} >= 31
       -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
%endif
       -DBUILD_TESTING:BOOL=ON \
       -DSPHINX_MAN:BOOL=ON .
make %{?_smp_mflags}

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}
rm %{buildroot}%{_pkgdocdir}/LICENSE
rm %{buildroot}%{_pkgdocdir}/NOTICE

%check
ctest %{?_smp_mflags}

%files
%{_bindir}/castxml
%doc %{_mandir}/man1/castxml.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/clang
%{_datadir}/%{name}/detect_vs.c
%{_datadir}/%{name}/detect_vs.cpp
%{_datadir}/%{name}/empty.c
%{_datadir}/%{name}/empty.cpp
%license LICENSE NOTICE

%changelog
* Tue Feb 18 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.1-1
- Update to version 0.3.1
- Drop cling-cpp.so linking patch - accepted upstream

* Sat Feb 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.0-1
- Update to version 0.3.0

* Wed Jan 29 2020 Tom Stellard <tstellar@redhat.com> - 0.2.0-5
- Link against libclang-cpp.so
- https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.0-3
- Backport clang 9 test fix

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.0-1
- First tagged release from upstream

* Tue Mar 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.29.20190117git9c91919
- Update sphinx BR

* Mon Feb 25 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.28.20190117git9c91919
- New git snapshot (supports LLVM8)
- Drop castxml-shared.patch in favor of new LLVM_LINK_LLVM_DYLIB cmake option

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.27.20180806gitae93121
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.26.20180806gitae93121
- Add source directory to cmake command

* Thu Aug 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.25.20180806gitae93121
- New git snapshot (supports LLVM7)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20180122git6952441
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20180122git6952441
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.22.20180122git6952441
- New git snapshot (supports LLVM6)
- Remove BuildRequires on llvm-static - llvm's cmake files have been fixed

* Wed Dec 13 2017 Tom Stellard <tstellar@redhat.com> - 0.1-0.21.20171013git367e90c
- Rebuild for LLVM 5.0

* Wed Oct 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.20.20171013git367e90c
- New git snapshot (supports LLVM5)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.20170301gitfab9c47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20170301gitfab9c47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1-0.17.20170301gitfab9c47
- Rebuild for LLVM4

* Wed Mar 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.16.20170301gitfab9c47
- New git snapshot
- Remove bundled provides for kwsys components - no longer used
- Rebuild for LLVM 3.9 (Fedora 25)

* Wed Feb 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.15.20170113gite7252f5
- New git snapshot

* Mon Nov 07 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.14.20161006git05db76f
- Rebuild for LLVM 3.9 (Fedora 26)

* Tue Oct 25 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.13.20161006git05db76f
- New git snapshot

* Fri Jul 01 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.12.20160617gitd5934bd
- New git snapshot

* Thu May 26 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.11.20160510git9a83414
- New git snapshot

* Thu Feb 25 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.10.20160125gitfc71eb9
- Adjust to llvm library changes again (the split was revoked)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20160125gitfc71eb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.8.20160125gitfc71eb9
- New git snapshot
- Properly adjust to the new llvm library split

* Wed Jan 27 2016 Adam Jackson <ajax@redhat.com> 0.1-0.7.20150924git552dd69
- Rebuild for llvm 3.7.1 library split

* Fri Sep 25 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.6.20150924git552dd69
- Adjust gccxml obsolete version

* Thu Sep 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.5.20150924git552dd69
- New git snapshot
- Allow warnings about guessing the float ABI during tests (fixes tests on arm)

* Thu Sep 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.4.20150902git7acd634
- New git snapshot

* Fri Aug 21 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.3.20150820git2e55b35
- New git snapshot
- Upstream has deleted the parts of the bundled kwsys sources that are not
  used by castxml from the source repository
- Add bundled provides for the remaining kwsys components according to
  revised FPC decision 2015-08-20
  https://fedorahosted.org/fpc/ticket/555

* Fri Aug 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.2.20150807git8a08a44
- New git snapshot
- Unbundle kwsys library according to FPC decision 2015-08-06
  https://fedorahosted.org/fpc/ticket/555

* Tue Apr 14 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.1.20150414git43fa139
- First packaging for Fedora
