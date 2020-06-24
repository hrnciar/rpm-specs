%{?nodejs_find_provides_and_requires}

Name:           nodejs-libpq
Version:        1.8.9
Release:        3%{?dist}
Summary:        Node native bindings to the PostgreSQL libpq C client library

License:        MIT
URL:            https://www.npmjs.com/package/libpq
Source0:        https://registry.npmjs.org/libpq/-/libpq-%{version}.tgz
# Patch out use of buffer-from shim
Patch0:         nodejs-libpq-bufferfrom.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp
BuildRequires:  libpq-devel
BuildRequires:  npm(nan)

BuildRequires:  npm(mocha)
BuildRequires:  npm(async)
BuildRequires:  npm(bindings)
BuildRequires:  npm(lodash)
BuildRequires:  npm(okay)
BuildRequires:  postgresql-test-rpm-macros


%description
Node native bindings to the PostgreSQL libpq C client library. This module
attempts to mirror as closely as possible the C API provided by libpq and
provides the absolute minimum level of abstraction. It is intended to be
extremely low level and allow you the same access as you would have to libpq
directly from C, except in node.js! The obvious trade-off for being "close to
the metal" is having to use a very "c style" API in JavaScript.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep bindings "^1.2.1"
%nodejs_fixdep --dev --move nan
rm -rf node_modules


%build
%nodejs_symlink_deps --build
%set_build_flags
node-gyp configure
node-gyp build


%install
mkdir -p %{buildroot}%{nodejs_sitearch}/libpq
cp -pr package.json index.js %{buildroot}%{nodejs_sitearch}/libpq
mkdir -p %{buildroot}%{nodejs_sitearch}/libpq/build
cp -p build/Release/addon.node %{buildroot}%{nodejs_sitearch}/libpq/build
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%postgresql_tests_run
%{_bindir}/mocha -t 20000


%files
%doc README.md
%{nodejs_sitearch}/libpq


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Tom Hughes <tom@compton.nu> - 1.8.9-1
- Update to 1.8.9 upstream release

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 1.8.8-5
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Pavel Raiskup <praiskup@redhat.com> - 1.8.8-3
- Use new postgres test macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 1.8.8-1
- Update to 1.8.8 upstream release

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 1.8.7-2
- Rebuild for Node.js 10.5.0

* Tue Mar  6 2018 Tom Hughes <tom@compton.nu> - 1.8.7-1
- Initial build of 1.8.7
