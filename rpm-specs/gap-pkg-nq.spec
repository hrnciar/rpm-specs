%global pkgname nq

Name:           gap-pkg-%{pkgname}
Version:        2.5.4
Release:        5%{?dist}
Summary:        Nilpotent Quotients of finitely presented groups

License:        GPLv2+
URL:            https://gap-packages.github.io/nq/
Source0:        https://github.com/gap-packages/nq/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
# Work around autodoc's inability to deal with line breaks in a subtitle
Patch0:         %{name}-doc.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gcc
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)

Requires:       gap-core%{?_isa}
Requires:       gap-pkg-polycyclic

%description
This package provides access from within GAP to the ANU nilpotent
quotient program for computing nilpotent factor groups of finitely
presented groups.

%package doc
Summary:        NQ documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
export CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
%configure --with-gaproot=%{_gap_dir} --disable-silent-rules

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

make %{?_smp_mflags}
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -a bin doc examples gap tst VERSION *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/test

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README
%license COPYING
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%changelog
* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 2.5.4-5
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 2.5.4-2
- Rebuild for changed bin dir name in gap 4.10.1

* Sat Feb 16 2019 Jerry James <loganjerry@gmail.com> - 2.5.4-1
- New upstream version (bz 1677807)
- Add -doc patch
- Add -doc subpackage
- Fix check script

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 2.5.3-1
- New upstream version (bz 1315678)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- New upstream version (bz 1296735)
- Update URLs

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 2.5.1-2
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Fri Jun 19 2015 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- Initial RPM
