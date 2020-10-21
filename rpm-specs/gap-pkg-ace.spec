%global pkgname ace

Name:           gap-pkg-%{pkgname}
Version:        5.3
Release:        3%{?dist}
Summary:        Advanced Coset Enumerator

License:        MIT
URL:            https://gap-packages.github.io/ace/
Source0:        https://github.com/gap-packages/ace/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  perl-interpreter
BuildRequires:  tth

# The code invokes echo and uname
Requires:       coreutils
Requires:       gap-core%{?_isa}

%description
The ACE package provides a mechanism to replace GAP's usual Todd-Coxeter
coset enumerator by ACE, so that functions that behind the scenes use
coset enumeration will use the ACE enumerator.  The ACE enumerator may
also be used explicitly; both non-interactively and interactively.
However the package is used, a plethora of options and strategies are
available to assist the user in avoiding incomplete coset enumerations.

%package doc
Summary:        Advanced Coset Enumerator documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Remove a reference to an obsolete BiBTeX file and an obsolete manual
sed -i 's|\.\./\.\./\.\./doc/mrabbrev,||;/doc\/ext/d' doc/manual.tex

%build
# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{_gap_dir}
make %{?_smp_mflags} EXTRA_CFLAGS="%{optflags}" LDFLAGS="$RPM_LD_FLAGS"

# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
ln -s %{_gap_dir}/etc ../../etc
make doc
rm -f ../../{doc,etc}

# Package PDF instead of PostScript
pushd standalone-doc
ps2pdf ace3001.ps ace3001.pdf
popd

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{CHANGES.md,configure,LICENSE,Makefile*,README.md,doc/make_doc,gap/CHANGES}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{doc/test,src,standalone-doc}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/res-examples/

%files doc
%doc standalone-doc/ace3001.pdf
%license LICENSE
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/res-examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/res-examples/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 5.3-2
- Rebuild for gap 4.11.0

* Wed Feb 12 2020 Jerry James <loganjerry@gmail.com> - 5.3-1
- Version 5.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 5.2-9
- Rebuild for changed bin dir name in gap 4.10.1

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 5.2-8
- Rebuild for gap 4.10.0
- Package PDF documentation instead of PostScript

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Jerry James <loganjerry@gmail.com> - 5.2-1
- Initial RPM
