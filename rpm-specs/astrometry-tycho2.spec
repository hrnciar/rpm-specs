# Files are no executable binaries but data, therefore we have nothing
# to generate debuginfo from.
%global debug_package %{nil}

Name:           astrometry-tycho2
Version:        2.0
Release:        9%{?dist}
Summary:        Tycho-2 catalogue for astrometry.net

License:        BSD
URL:            https://github.com/lupinix/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  astrometry
BuildRequires:  python3-astropy

Requires:       astrometry

# Astrometry build on s390 has been temporarily disabled
ExcludeArch:    s390x

%description
Tycho-2 catalogue for the astrometry.net solver

%prep
%autosetup


%build
%make_build


%install
make install DESTDIR=%{buildroot}/usr


%files
%license LICENSE.txt cat/COPYRIGHT
%doc cat/ReadMe cat/guide.pdf
%{_datadir}/astrometry/data/*.fits


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Mattia Verga <mattia.verga@protonmail.com> - 2.0-8
- Temporarily disable s390 due to astrometry dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Christian Dersch <lupinix@mailbox.org> - 2.0-2
- Removed BuildArch: noarch as the resulting FITS depend on endianess

* Mon Oct 16 2017 Christian Dersch <lupinix@mailbox.org> - 2.0-1
- new version

* Wed Jul 12 2017 Christian Dersch <lupinix@mailbox.org> - 1.1.1-1
- initial release
