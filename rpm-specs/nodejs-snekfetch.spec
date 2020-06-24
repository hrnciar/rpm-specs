# Note: this has been deprecated by nodejs-(node-)fetch
# but is still required by older versions of things.

%global npmname snekfetch

Name:           nodejs-%{npmname}
Version:        4.0.4
Release:        4%{?dist}
Summary:        Fast, efficient, and user-friendly http requests

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

BuildRequires:  nodejs-packaging

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Snekfetch is a fast, efficient, and user-friendly library for making
HTTP requests.

It also supports native ALPN negotiation in node for efficient http/2
requests!

The API was inspired by superagent, however it is much smaller and
faster. In fact, in browser, it is a mere 4.0kb.

%prep
%autosetup -n package

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a src/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 4.0.4-1
- Initial package.
