%global service rust2rpm

Name:           obs-service-%{service}
Version:        1
Release:        3%{?dist}
Summary:        OBS source service: Generate rpm packaging for Rust crates

License:        MIT
URL:            https://pagure.io/fedora-rust/%{name}
Source0:        https://releases.pagure.org/fedora-rust/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  rust-srpm-macros >= 9
Requires:       rust2rpm >= 9
Supplements:    ((obs-source_service or osc) and rust2rpm)

BuildArch:      noarch
ExclusiveArch:  %{rust_arches} noarch

%description
This is a source service for openSUSE Build Service.

This simply runs rust2rpm for a given Rust crate on crates.io
to generate RPM packaging to build packages for crates.

%prep
%autosetup


%build
# Nothing to build

%install
%make_install


%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/rust2rpm*
%dir %{_localstatedir}/cache/obs
%dir %{_localstatedir}/cache/obs/rust2rpm

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May  5 07:51:56 EDT 2019 Neal Gompa <ngompa13@gmail.com> - 1-1
- Initial packaging for Fedora (RH#1706555)
