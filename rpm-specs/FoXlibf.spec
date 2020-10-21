# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global upstream_name FoX

Name:		FoXlibf
Version:	4.1.2
Release:	13%{?dist}
Summary:	A Fortran XML Library
License:	zlib and BSD
URL:		http://www1.gly.bris.ac.uk/~walker/FoX/
Source0:	http://www1.gly.bris.ac.uk/~walker/FoX/source/%{upstream_name}-%{version}.tar.gz
Patch0:		FoX-4.1.2-DESTDIR.patch
Patch1:		FoX-4.1.2-system-paths.patch
Patch2:		FoX-4.1.2-sharedlibs.patch
Patch3:		FoX-4.1.2-dompp.patch
BuildRequires:	gcc-gfortran

%description
FoX is an XML library written in Fortran 95. It allows software developers to
read, write and modify XML documents from Fortran applications without the 
complications of dealing with multiple language development.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for FoX

%description devel
Development files for FoX.

%package static
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Static libraries for FoX

%description static
Static libraries for FoX.

%prep
%setup -qn %{upstream_name}-%{version}
%patch0 -p1 -b .DESTDIR
%patch1 -p1 -b .system
%patch2 -p1 -b .shared

# We need a variant "pretty-print" version of the dom library for exciting
cp -a dom dompp
sed -i "s/ 27293398$/ ibset(27293398,22)/" dompp/m_dom_dom.F90 
sed -i "s|libFoX_dom|libFoX_dompp|g" dompp/makefile

%patch3 -p1 -b .dompp

%build
export FCFLAGS="%{optflags} %{?_fmoddir: -I%_fmoddir} -fPIC"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
pushd %{buildroot}%{_libdir}
for i in libFoX_common libFoX_dom libFoX_dompp libFoX_fsys libFoX_sax libFoX_utils libFoX_wcml libFoX_wkml libFoX_wxml; do
	ln -s $i.so.0.0.0 $i.so.0
	ln -s $i.so.0.0.0 $i.so
done
chmod -x %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc README.FoX.txt
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libFoX*.so.*

%files devel
%{_bindir}/FoX-config
%{_includedir}/FoX/
%{_libdir}/libFoX*.so

%files static
%{_libdir}/libFoX*.a

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Oct 31 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 4.1.2-5
- Rebuilt for new gcc-gfortran on el7

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Marcin Dulak <Marcin.Dulak@gmail.com> - 4.1.2-2
- rebuild for gcc-gfortran-5.0.0

* Sat Nov 8 2014 Marcin Dulak <Marcin.Dulak@gmail.com> - 4.1.2-1
- renamed to FoXlibf

* Thu May 29 2014 Tom Callaway <spot@fedoraproject.org> - 4.1.2-1
- initial package
