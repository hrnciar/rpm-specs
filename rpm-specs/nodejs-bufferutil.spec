%global npmname bufferutil

Name:           nodejs-%{npmname}
Version:        4.0.1
Release:        3%{?dist}
Summary:        WebSocket buffer utils

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

# Pull sources from github, not npm, in order to include unit tests.
Source0:	https://github.com/websockets/%{npmname}/archive/v%{version}/%{name}-%{version}.tar.gz
# Revert to using bindings instead of prebuildify
Patch0:         nodejs-bufferutil-bindings.patch        

BuildRequires:  nodejs-packaging
BuildRequires:  node-gyp, nodejs-bindings

BuildRequires:  nodejs-nan

# For unit tests.
BuildRequires:  mocha

ExclusiveArch:  %{nodejs_arches}

%description
bufferutil provides some utilities to efficiently perform
some operations such as masking and unmasking the data
payload of WebSocket frames.

%prep
%autosetup -p 1 -n %{npmname}-%{version}


%build
%nodejs_symlink_deps --build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,undefs"
node-gyp rebuild


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/bufferutil/build
cp -p package.json fallback.js index.js %{buildroot}%{nodejs_sitelib}/bufferutil/
cp -p build/Release/bufferutil.node %{buildroot}%{nodejs_sitelib}/bufferutil/build/
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
mocha ./test.js


%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 15 2019 Tom Hughes <tom@compton.nu> - 4.0.1-1
- Update to 4.0.1 upstream release

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 3.0.5-6
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 3.0.5-3
- Rebuild for Node.js 10.5.0

* Mon May 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 3.0.5-1
- Updated to latest upstream release (rhbz#1564474).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Tom Hughes <tom@compton.nu> - 3.0.3-5
- Convert nan to a devDependency

* Fri Feb 02 2018 Ben Rosser <rosser.bjr@gmail.com> - 3.0.3-4
- Invoke nodejs_fixdep nan. This dependency has since been updated upstream.

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 3.0.3-3
- Export LDFLAGS for hardened build support
- Allow undefined symbols in the shared object

* Sat Nov 25 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.0.3-2
- Since the unit tests passed, allow any nodejs-bindings.

* Fri Nov 03 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.0.3-1
- Update to latest upstream release (#1509251).

* Tue Aug 22 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.0.2-4
- Rebuild against new nodejs.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.0.2-1
- Rebuild against nodejs 8 and update to latest upstream release.

* Wed May 31 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.0.1-1
- Update to latest upstream release.

* Tue Mar 14 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.0.0-1
- Update to latest upstream release, including unit tests.

* Sun Feb 26 2017 Ben Rosser <rosser.bjr@gmail.com> - 2.0.1-1
- Initial package.
