%global npmname net-browserify-alt

Name:           nodejs-%{npmname}
Version:        1.1.0
Release:        7%{?dist}
Summary:        A port of the net module for the browser

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}
Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-ws, nodejs-body-parser, nodejs-bufferutil

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
net module for browserify, with a websocket server proxy. Supported methods:

net.connect(options, cb)
net.isIP(input), net.isIPv4(input), net.isIPv6(input)

Examples are available in examples/.

%prep
%autosetup -n package

%nodejs_fixdep bufferutil
%nodejs_fixdep body-parser
%nodejs_fixdep ws

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a api.js browser.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md examples/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-1
- Initial package.
