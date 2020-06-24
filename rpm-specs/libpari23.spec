Name:		libpari23
Version:	2.3.5
Release:	18%{?dist}
Summary:	Number Theory-oriented Computer Algebra Library
# No version is specified
License:	GPL+
URL:		http://pari.math.u-bordeaux.fr/
Source0:	http://pari.math.u-bordeaux.fr/pub/pari/OLD/2.3/pari-%{version}.tar.gz
Patch1:		libpari23-optflags.patch
Patch2:		libpari23-fsf-address.patch
Patch3:		Math-Pari-2.01080604-extra-stack-for-test.patch
Patch4:		pari-2.3.5-Fix-build-with-no-dot-in-INC.patch
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	perl-interpreter
BuildRequires:	perl(lib)
BuildRequires:	readline-devel
BuildRequires:	sed
BuildRequires:	tex(tex)
BuildRequires:	tex(dvips)
BuildRequires:	xmkmf

# Avoid doc-file dependencies and provides
%global __provides_exclude_from ^%{_datadir}/pari/PARI/
%global __requires_exclude_from ^%{_datadir}/pari/PARI/

%description
PARI is a widely used computer algebra system designed for fast computations in
number theory (factorizations, algebraic number theory, elliptic curves...),
but also contains a large number of other useful functions to compute with
mathematical entities such as matrices, polynomials, power series, algebraic
numbers, etc., and a lot of transcendental functions.

This is an old version of the library, for compatibility with applications and
library bindings that have not been migrated to the current stable release.

%package devel
Summary:	Header files and libraries for PARI development
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Header files and libraries for PARI development with the old version 2.3.x
API.

%prep
%setup -q -n pari-%{version}

# Use our optflags, not upstream's
%patch1
sed -i -e 's|@OPTFLAGS@|%{optflags} -fPIC|' config/get_cc

# Update FSF address in copyright notices
%patch2 -p1

# perl-Math-Pari uses libpari23's test suite but needs more stack on some architectures
%patch3 -p2

# Fix build for Perls without '.' in @INC
%patch4

# Avoid unwanted rpaths
sed -i "s|runpathprefix='.*'|runpathprefix=''|" config/get_ld

# Fix up shellbangs
sed -i "s|@perl@|%{__perl}|" doc/gphelp.in misc/tex2mail.in

# Create a pkg-config file
cat > libpari23.pc << __EOF__
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}
datadir=%{_datadir}
paridir=%{_datadir}/%{name}

Name: Libpari23
Description: Number Theory-oriented Computer Algebra Library.
URL: http://pari.math.u-bordeaux.fr/
Version: %{version}
Libs: -lpari23
Cflags: -I\${includedir}/%{name}
__EOF__

%build
./Configure \
    --prefix=%{_prefix} \
    --share-prefix=%{_datadir} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir}/man1 \
    --datadir=%{_datadir}/pari \
    --without-gmp
make %{?_smp_mflags} all

%install
make install \
	DESTDIR=%{buildroot} \
	INSTALL="install -p" \
	STRIP=/bin/true

# we move pari.cfg to the docdir
rm -rf %{buildroot}%{_prefix}/lib/pari

# We'll link to this library as libpari23 rather than libpari
mv %{buildroot}%{_libdir}/libpari{.so,23.so}

# Move header files to avoid conflicting with pari-devel
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/{pari,%{name}/pari}

# Install tests and documentation, needed e.g. by perl-Math-Pari
mkdir -p %{buildroot}%{_datadir}/%{name}/src/
cp -a src/test/ %{buildroot}%{_datadir}/%{name}/src/
cp -a doc %{buildroot}%{_datadir}/%{name}/

# Additional headers needed e.g. by perl-Math-Pari
mkdir -p %{buildroot}%{_datadir}/%{name}/src/{graph,gp,headers,language}/
cp -a src/graph/*.h %{buildroot}%{_datadir}/%{name}/src/graph/
cp -a src/gp/*.h %{buildroot}%{_datadir}/%{name}/src/gp/
cp -a src/headers/*.h %{buildroot}%{_datadir}/%{name}/src/headers/
cp -a src/language/*.h %{buildroot}%{_datadir}/%{name}/src/language/

# Install our pkg-config file so the library can be found
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
cp -p libpari23.pc %{buildroot}%{_libdir}/pkgconfig/

# Remove emacs support files if built on a system with emacs
rm -rf %{buildroot}%{_datadir}/emacs/site-lisp/pari/

# Placate rpmlint regarding binary and library permissions
%{_fixperms} %{buildroot}{%{_bindir},%{_libdir}}

%check
make dobench
make dotest-compat
make dotest-intnum
make dotest-qfbsolve
make dotest-rfrac
make dotest-round4

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS CHANGES* COMPAT NEW README
%doc Olinux-*/pari.cfg
%{_libdir}/libpari.so.%{version}
%{_libdir}/libpari.so.2

# Files for the pari-gp calculator, which we don't ship
%exclude %{_bindir}/gp
%exclude %{_bindir}/gp-2.3
%exclude %{_bindir}/gphelp
%exclude %{_bindir}/tex2mail
%exclude %doc %{_datadir}/pari/PARI/
%exclude %doc %{_datadir}/pari/doc/
%exclude %doc %{_datadir}/pari/examples/
%exclude %{_datadir}/pari/misc/
%exclude %{_datadir}/pari/pari.desc
%exclude %{_mandir}/man1/gp-2.3.1*
%exclude %{_mandir}/man1/gp.1*
%exclude %{_mandir}/man1/gphelp.1*
%exclude %{_mandir}/man1/pari.1*
%exclude %{_mandir}/man1/tex2mail.1*

%files devel
%{_includedir}/%{name}/pari/
%{_libdir}/libpari23.so
%{_libdir}/pkgconfig/libpari23.pc
%{_datadir}/%{name}/

%changelog
* Tue Feb  4 2020 Paul Howarth <paul@city-fan.org> - 2.3.5-18
- Update optflags patch to support GCC 10 and above
- Upstream shuffled files around, update source URL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Paul Howarth <paul@city-fan.org> - 2.3.5-13
- Switch to %%ldconfig_scriptlets
- Use %%license
- Fix up shellbangs
- Specify all build requirements
- Update URL

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Paul Howarth <paul@city-fan.org> - 2.3.5-11
- Fix build for Perls without '.' in @INC
- Drop redundant Group: tags
- Build without GMP, which seems to cause problems for Math::Pari on 32-bit
  architectures with -Duse64bitint (#1459155)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Paul Howarth <paul@city-fan.org> - 2.3.5-2
- Incorporate changes from package review (#837004)
  - Remove %%clean section and cleaning of buildroot in %%install
  - Build with -fPIC
  - Update FSF address in copyright notices
  - Remove emacs support files if built on a system with emacs

* Wed Jun 13 2012 Paul Howarth <paul@city-fan.org> - 2.3.5-1
- Initial RPM version
