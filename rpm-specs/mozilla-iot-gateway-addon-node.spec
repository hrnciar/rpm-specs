%global npm_name gateway-addon-node
%global debug_package %{nil}
%{?nodejs_find_provides_and_requires}

# don't require bundled modules
%global __requires_exclude_from ^%{_prefix}/lib/node_modules/gateway-addon-node/.*$

Name:          mozilla-iot-gateway-addon-node
Version:       0.9.0
Release:       2%{?dist}
Summary:       Node bindings for Mozilla IoT Gateway
## Licenses
# MPLv2.0 : mozilla-iot-gateway-addon-node 
# BSD : uri-js (bundled)
# MIT : ajv  fast-deep-equal punycode (all bundled)
# MIT : fast-json-stable-stringify json-schema-traverse  (all bundled)
License:       MPLv2.0 and BSD and MIT
URL:           https://github.com/mozilla-iot/gateway-addon-node
# Source0 was created by running gateway-addon-node-tarball.sh
Source0:       gateway-addon-node-v%{version}.tar.gz
Source1:       gateway-addon-node-tarball.sh

ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

BuildRequires: nodejs-packaging
## All the unbundled node modules - Required
Requires:      npm(sqlite3)
## All the bundled node modules  - Provides: bundled
Provides:      bundled(ajv) = 6.8.1
Provides:      bundled(fast-deep-equal) = 2.0.1
Provides:      bundled(fast-json-stable-stringify) = 2.0.0
Provides:      bundled(json-schema-traverse) = 0.4.1
Provides:      bundled(punycode) = 2.1.1
Provides:      bundled(uri-js) = 4.2.2


%description
Node bindings for Node add-ons for Mozilla IoT Gateway.


%prep
%autosetup -n %{npm_name}-%{version}

# Clean up hidden files
find node_modules -name .travis.yml -delete
find node_modules -name .eslintrc.yml -delete
find node_modules -name .npmignore -delete
find node_modules -name .yarn-integrity -delete
find node_modules -name .tonic_example.js -delete
find node_modules -name .DS_Store -delete

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js lib node_modules package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Troy Dawson <tdawson@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Troy Dawson <tdawson@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Feb 08 2019 Troy Dawson <tdawson@redhat.com> - 0.4.0-1
- Initial build with 0.4.0
- Bundle nodejs dependencies
- Unbundle binary (arch dependant) modules, add Requires for these.
- Include licenses and Provides for bundled modules
