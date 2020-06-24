%{?nodejs_find_provides_and_requires}

%global cli_version 4.17.5

Name:           lodash
Version:        4.17.15
Release:        4%{?dist}
Summary:        A JavaScript utility library

License:        MIT
URL:            https://lodash.com/
Source0:        https://github.com/lodash/lodash/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/lodash/lodash-cli/archive/%{cli_version}/%{name}-cli-%{cli_version}.tar.gz
Source2:        https://raw.githubusercontent.com/lodash/lodash/%{version}-npm/package.json#/%{name}-package-%{version}.json
Source3:        %{name}-modules.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Obsoletes:      nodejs-lodash-compat < 3.10.1-14
Obsoletes:      nodejs-lodash-node < 3.10.1-14

BuildRequires:  nodejs-packaging >= 7-5
BuildRequires:  web-assets-devel

BuildRequires:  npm(closure-compiler)
BuildRequires:  npm(glob)
BuildRequires:  npm(uglify-js) >= 2.4.13
BuildRequires:  npm(semver)


%description
A JavaScript utility library delivering consistency,
modularity, performance, & extras.


%package -n js-lodash
Summary:        The modern build of lodash modular utilities
Requires:       %{name} = %{version}-%{release}
Requires:       web-assets-filesystem

%description -n js-lodash
The modern build of lodash exported as a single file.


%package -n nodejs-lodash
Summary:        The modern build of lodash modular utilities
Requires:       %{name} = %{version}-%{release}

%description -n nodejs-lodash
The modern build of lodash exported as Node.js/io.js modules.


%package -n nodejs-lodash-cli
Summary:        The lodash command-line interface
Requires:       %{name} = %{version}-%{release}
Version:        %{cli_version}
Release:        %{version}.%{release}

%description -n nodejs-lodash-cli
The lodash command-line interface for creating custom
builds & precompiling templates


%{lua:
template = [[
%%package -n nodejs-lodash-@@PKG@@
Summary:        The modern build of lodash's _.@@FUNC@@ as a module

%%description -n nodejs-lodash-@@PKG@@
The modern build of lodash's _.@@FUNC@@ as a module.

%%files -n nodejs-lodash-@@PKG@@
%%doc npm/lodash.@@FUNC@@/README.md
%%license npm/lodash.@@FUNC@@/LICENSE
%{nodejs_sitelib}/lodash.@@FUNC@@
]]
for func in io.open(rpm.expand("%SOURCE3")):lines() do
  pkg = string.gsub(func, "_", "")
  print(rpm.expand(string.gsub(string.gsub(template, "@@FUNC@@", func), "@@PKG@@", pkg)).."\n")
end}


%prep
%setup -q -T -b 0 -a 1
rm -rf node_modules vendor
pushd %{name}-cli-%{version}
  %nodejs_fixdep closure-compiler "^0.2.6"
  %nodejs_fixdep glob "^6.0.3"
  %nodejs_fixdep -r lodash
  %nodejs_fixdep semver "^5.1.0"
  %nodejs_fixdep uglify-js "^2.4.13"
  rm -rf node_modules
popd
mkdir node_modules
mv %{name}-cli-%{version} node_modules/lodash-cli


%build
# Setup lodash-cli dependencies
pushd node_modules/lodash-cli
  %nodejs_symlink_deps --build
  ln -sf ../../.. node_modules/lodash
popd
# Build generic single file versions
%{__nodejs} ./node_modules/lodash-cli/bin/lodash -o ./dist/lodash.js
# Build lodash npm module
mkdir nodejs-lodash
pushd nodejs-lodash
  %{__nodejs} ../node_modules/lodash-cli/bin/lodash modularize exports=node -o ./
  %{__nodejs} ../node_modules/lodash-cli/bin/lodash -d -o ./lodash.js
popd
# Build split npm modules
%{__nodejs} ./node_modules/lodash-cli/bin/lodash modularize exports=npm -d -o ./npm


%install
mkdir -p %{buildroot}%{nodejs_sitelib}
# Install generic single file versions
mkdir -p %{buildroot}%{_jsdir}/lodash
cp -p dist/lodash.js dist/lodash.min.js %{buildroot}%{_jsdir}/lodash
# Install lodash npm module
cp -pr nodejs-lodash %{buildroot}%{nodejs_sitelib}/lodash
cp -pr %{SOURCE2} %{buildroot}%{nodejs_sitelib}/lodash/package.json
# Install lodash-cli npm module
mkdir -p %{buildroot}%{_datadir}/nodejs-lodash-cli
cp -pr node_modules/lodash-cli/template %{buildroot}%{_datadir}/nodejs-lodash-cli
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash-cli
cp -pr node_modules/lodash-cli/package.json %{buildroot}%{nodejs_sitelib}/lodash-cli
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash-cli/lib
install -p -m644 node_modules/lodash-cli/lib/* %{buildroot}%{nodejs_sitelib}/lodash-cli/lib
ln -s %{_datadir}/nodejs-lodash-cli/template %{buildroot}%{nodejs_sitelib}/lodash-cli
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash-cli/bin
install -p -m755 node_modules/lodash-cli/bin/* %{buildroot}%{nodejs_sitelib}/lodash-cli/bin
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/lodash-cli/bin/lodash %{buildroot}%{_bindir}
# Install split npm modules
pushd npm
  for module in lodash.*
  do
    mkdir %{buildroot}%{nodejs_sitelib}/$module
    cp -pr $module/package.json %{buildroot}%{nodejs_sitelib}/$module
    cp -pr $module/index.js %{buildroot}%{nodejs_sitelib}/$module
  done
popd
# Setup dependencies
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check


%files
%doc README.md
%license LICENSE


%files -n js-lodash
%{_jsdir}/lodash


%files -n nodejs-lodash
%{nodejs_sitelib}/lodash


%files -n nodejs-lodash-cli
%{nodejs_sitelib}/lodash-cli
%{_datadir}/nodejs-lodash-cli
%{_bindir}/lodash


%changelog
* Mon May 11 2020 Tom Hughes <tom@compton.nu> - 4.17.15-4
- Fix nodejs-lodash-cli dependency on lodash

* Mon Mar  2 2020 Tom Hughes <tom@compton.nu> - 4.17.15-3
- Restore dist tag in nodejs-load-cli subpackage

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Tom Hughes <tom@compton.nu> - 4.17.15-1
- Update to 4.17.15 upstream release

* Sun Sep  1 2019 Tom Hughes <tom@compton.nu> - 3.10.1-13
- Remove workaround for long fixed RPM bug
- Modernise spec file

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 3.10.1-5
- Update npm(semver) dependency

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 3.10.1-4
- Update glob dependency

* Mon Dec 14 2015 Tom Hughes <tom@compton.nu> - 3.10.1-3
- Correct paths in nodejs-lodash module

* Sun Dec 13 2015 Tom Hughes <tom@compton.nu> - 3.10.1-2
- Make base package require fully versioned

* Sun Nov 15 2015 Tom Hughes <tom@compton.nu> - 3.10.1-1
- Intial build of 3.10.1
