## disable empty debuginfo package
%global debug_package %{nil}

Name:           gela-asis
Version:        0.3.3
Release:        6%{?dist}
Summary:        Implementation of ASIS
License:        BSD
URL:            http://gela.ada-ru.org/gela_asis
Source0:        http://www.ada-ru.org/files/gela-asis-%{version}.tar.bz2
BuildRequires:  gcc-gnat chrpath fedora-gnat-project-common > 3
BuildRequires:  gprbuild
# gprbuild only available on these:
ExclusiveArch:   %GPRbuild_arches



%description
Platform/compiler independent implementation of Ada
Semantic Interface Specification. 

%package devel
Summary:        Devel package for %{name}
License:        BSD
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common > 3 

%description devel
%{summary}


%prep
%setup -q

%build
export FLAGS="%GNAT_optflags"
make %{?_smp_mflags} LIBKIND="relocatable"


%install
mkdir -p %{buildroot}/%_GNAT_project_dir
make install DESTDIR=%{buildroot} \
PREFIX=%{_prefix} LIBDIR=%{_libdir} \
LIBKIND="relocatable" GELA_INCLUDE_PATH=%{_includedir}/%{name} \
GPRDIR=%_GNAT_project_dir LIB=%{_libdir}/%{name} GPR=fedora.gpr.in
chrpath --delete %{buildroot}/%{_libdir}/%{name}/*.so*
cd %{buildroot}/%{_libdir} && for i in `ls gela-asis/*.so*`; do ln -s $i `basename $i`; done

%ldconfig_scriptlets

%files
%doc COPYING
%dir %{_libdir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}/lib%{name}.so

%files devel
%doc README.txt
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/spec/
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/%{name}/lib%{name}.so.%{version}
%{_includedir}/%{name}/*.ad[sb]
%{_includedir}/%{name}/spec/*.ad[sb]
%{_libdir}/%{name}/*.ali
%_GNAT_project_dir/gela_asis.gpr


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3.3-2
- New version v0.3.3
- Fix Arch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3.2-2
- Change URL tag 

* Sun Dec 01 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3.2-1
- Bugfix release. 

* Wed Nov 27 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3.1-2
- Removing rpath 

* Thu Nov 21 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3.1-1
- Bugfix release update (patches have been accepted upstream)

* Thu Oct 24 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3-7
- Add BR
- Change arch list with macros

* Wed Oct 23 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3-6
- Add qtada patch
- Change library type 

* Tue Oct 22 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 0.3-4
- Initial build 
- Add ExclusiveArch 
- Fix rpmlint errors 
- Add missed ldconfig call


