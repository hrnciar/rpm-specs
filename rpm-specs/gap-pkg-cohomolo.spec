%global pkgname cohomolo

Name:           gap-pkg-%{pkgname}
Version:        1.6.8
Release:        4%{?dist}
Summary:        Cohomology groups of finite groups on finite modules

License:        GPLv2+
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Add missing shebangs
Patch0:         %{name}-shebang.patch
# Fix all -Wreturn-type warnings
Patch1:         0001-Eliminate-all-Wreturn-type-warnings.patch
# Fix all -Wmaybe-uninitialized warnings
Patch2:         0002-Eliminate-all-Wmaybe-uninitialized-warnings.patch
# Fix all -Wchar-subscripts warnings
Patch3:         0003-Eliminate-all-Wchar-subscripts-warnings.patch
# Fix all -Wunused-variable and -Wunused-but-set-variable warnings
Patch4:         0004-Eliminate-all-Wunused-variable-and-Wunused-but-set-v.patch
# Fix all -Wno-dangling-else warnings
Patch5:         0005-Eliminate-all-Wno-dangling-else-warnings.patch
# Fix the build with -fno-common
Patch6:         %{name}-fno-common.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc
BuildRequires:  tth

Requires:       gap-core

%description
This package may be used to perform certain cohomological calculations
on a finite permutation group G.  The following properties of G can be
computed:

1. The p-part Mul_p of the Schur multiplier Mul of G, and a presentation
   of a covering extension of Mul_p by G, for a specified prime p;

2. The dimensions of the first and second cohomology groups of G acting
   on a finite dimensional KG-module M, where K is a field of prime
   order; and

3. Presentations of split and nonsplit extensions of M by G.

%package doc
Summary:        Cohomolo documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Fix paths
sed -i 's,\.\./\.\./\.\./,/usr/lib/gap/,' doc/make_doc

%build
# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{_gap_dir}

# Build the binaries
%make_build CFLAGS="%{optflags}" LDFLAGS="$RPM_LD_FLAGS"

# Build the documentation
ln -s %{_gap_dir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/standalone
cp -a bin doc gap htm testdata tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -a standalone/{data.d,info.d} %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/standalone
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/make_doc
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 1.6.8-3
- Rebuild for gap 4.11.0

* Mon Feb  3 2020 Jerry James <loganjerry@gmail.com> - 1.6.8-2
- Add -fno-common patch to fix build with GCC 10
- Add 0001 through 0005 patches to eliminate warnings

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Jerry James <loganjerry@gmail.com> - 1.6.8-1
- Initial RPM
