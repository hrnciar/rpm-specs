%global pkgname  cvec

Name:           gap-pkg-%{pkgname}
Version:        2.7.4
Release:        6%{?dist}
Summary:        Compact vectors over finite fields

License:        GPLv2+
URL:            https://gap-packages.github.io/cvec/
Source0:        https://github.com/gap-packages/cvec/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb-doc
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc
BuildRequires:  libtool

Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

%description
The CVEC package provides an implementation of compact vectors over
finite fields.  Contrary to earlier implementations no table lookups are
used but only word-based processor arithmetic.  This allows for bigger
finite fields and higher speed.

%package doc
Summary:        CVEC documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-orb-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}
%setup -q -n %{pkgname}-%{version} -T -D -b 1

%build
export LC_ALL=C.UTF-8

# This is NOT an autotools-generated configure script; do NOT use %%configure
./configure %{_gap_dir}
%make_build V=1

# Build the documentation
make doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -p bin/%{_gap_arch}/.libs/cvec.so \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -a doc example gap local test tst *.g \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README.md TIMINGS TODO
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/example/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/example/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/example/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 2.7.4-5
- Drop aarch64 workaround

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 2.7.4-4
- Rebuild for gap 4.11.0
- Add atlasrep and tomlib BRs so that all tests can be run

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 2.7.4-1
- New upstream version

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 2.7.2-1
- New upstream version

* Mon Mar  4 2019 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- New upstream version

* Wed Feb 20 2019 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- New upstream version

* Tue Dec 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.6.1-1
- Initial package.
