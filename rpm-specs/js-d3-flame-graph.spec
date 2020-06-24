%global         pkgname d3-flame-graph
%global         github https://github.com/spiermar/d3-flame-graph

Name:           js-d3-flame-graph
Version:        3.0.2
Release:        1%{?dist}
Summary:        A D3.js plugin that produces flame graphs

BuildArch:      noarch

License:        ASL 2.0
URL:            %{github}

Source0:        %{github}/archive/%{version}/%{pkgname}-%{version}.tar.gz
Source1:        d3-flame-graph-deps-%{version}.tar.xz
Source2:        create_dependency_bundle.sh

BuildRequires:  web-assets-devel
BuildRequires:  nodejs
Requires:       web-assets-filesystem

# Bundled npm packages
Provides: bundled(nodejs-clean-webpack-plugin) = 3.0.0
Provides: bundled(nodejs-copy-webpack-plugin) = 5.1.1
Provides: bundled(nodejs-css-loader) = 3.4.2
Provides: bundled(nodejs-d3-array) = 2.4.0
Provides: bundled(nodejs-d3-dispatch) = 1.0.6
Provides: bundled(nodejs-d3-ease) = 1.0.6
Provides: bundled(nodejs-d3-format) = 1.4.3
Provides: bundled(nodejs-d3-hierarchy) = 1.1.9
Provides: bundled(nodejs-d3-scale) = 3.2.1
Provides: bundled(nodejs-d3-selection) = 1.4.1
Provides: bundled(nodejs-d3-transition) = 1.3.2
Provides: bundled(nodejs-eslint) = 6.8.0
Provides: bundled(nodejs-eslint-config-standard) = 14.1.0
Provides: bundled(nodejs-eslint-loader) = 3.0.3
Provides: bundled(nodejs-eslint-plugin-import) = 2.20.1
Provides: bundled(nodejs-eslint-plugin-node) = 11.0.0
Provides: bundled(nodejs-eslint-plugin-promise) = 4.2.1
Provides: bundled(nodejs-eslint-plugin-standard) = 4.0.1
Provides: bundled(nodejs-html-webpack-plugin) = 3.2.0
Provides: bundled(nodejs-script-ext-html-webpack-plugin) = 2.1.4
Provides: bundled(nodejs-style-loader) = 1.1.3
Provides: bundled(nodejs-tape) = 4.13.2
Provides: bundled(nodejs-terser-webpack-plugin) = 2.3.5
Provides: bundled(nodejs-webpack) = 4.42.0
Provides: bundled(nodejs-webpack-cli) = 3.3.11
Provides: bundled(nodejs-webpack-dev-server) = 3.10.3

%description
A D3.js plugin that produces flame graphs from hierarchical data.


%package doc
Summary: Documentation and example files for js-d3-flame-graph

%description doc
Documentation and example files for js-d3-flame-graph.


%prep
%setup -q -n %{pkgname}-%{version}
%setup -q -a 1 -n %{pkgname}-%{version}

%build
rm -rf dist
./node_modules/webpack/bin/webpack.js --mode production

%install
install -d -m 755 %{buildroot}/%{_datadir}/%{pkgname}
mv dist/templates/* %{buildroot}/%{_datadir}/%{pkgname}
rmdir dist/templates

install -d -m 755 %{buildroot}/%{_jsdir}/%{pkgname}
cp -a dist/* %{buildroot}/%{_jsdir}/%{pkgname}

%files
%{_jsdir}/%{pkgname}
%{_datadir}/%{pkgname}

%license LICENSE
%doc README.md

%files doc
%doc README.md examples

%changelog
* Fri Mar 20 2020 Andreas Gerstmayr <agerstmayr@redhat.com> 3.0.2-1
- initial version
