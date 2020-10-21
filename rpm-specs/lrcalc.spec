Name:		lrcalc
Version:	1.2
Release:	10%{?dist}
License:	GPLv2+
Summary:	Littlewood-Richardson Calculator
URL:		http://math.rutgers.edu/~asbuch/lrcalc
Source0:	http://math.rutgers.edu/~asbuch/lrcalc/%{name}-%{version}.tar.gz
Source1:	lrcalc.module.in
Requires:	environment(modules)
# sagemath patch
Patch0:		includes.patch

BuildRequires:  gcc-c++
%description
The "Littlewood-Richardson Calculator" is a package of C and Maple programs
for computing Littlewood-Richardson coefficients. The C programs form the
engine of the package, providing fast calculation of single LR coefficients,
products of Schur functions, and skew Schur functions. The Maple code mainly
gives an interface which makes it possible to use the C programs from Maple.
This interface uses the same notation as the SF package of John Stembridge,
to make it easier to use both packages at the same time.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure --bindir=%{_libdir}/%{name} --enable-shared --disable-static
# Kill rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_datadir}/%{name}/README
rm %{buildroot}%{_datadir}/%{name}/%{name}.maple

mkdir -p %{buildroot}%{_datadir}/modulefiles
sed 's#@BINDIR@#'%{_libdir}/%{name}'#g;' < %{SOURCE1} > \
    %{buildroot}%{_datadir}/modulefiles/%{name}-%{_arch} 

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir}: make check

%ldconfig_scriptlets

%files
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%license LICENSE
%doc README
%{_libdir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_datadir}/modulefiles/%{name}-%{_arch}

%files		devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2-1
- Update do latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.6-7
- Require environment(modules), install into generic modulefiles location
- Use %%license
- Drop group

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.6-2.beta
- Rebuild with updated upstream tarball (#909510#c3).

* Fri Feb  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.6-1.beta
- Initial lrcalc spec.
