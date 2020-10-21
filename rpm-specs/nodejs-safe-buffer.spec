Name:               nodejs-safe-buffer
Version:            5.2.1
Release:            1%{?dist}
Summary:            Node.js module for a safer buffer API

License:            MIT
URL:                https://github.com/feross/safe-buffer
Source0:            https://github.com/feross/safe-buffer/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:          noarch
ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging
BuildRequires:      npm(tape)

%description
%{summary}.

%prep
%autosetup -n safe-buffer-%{version}
rm -rf node_modules

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/safe-buffer
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/safe-buffer
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
tape test/*.js

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/safe-buffer

%changelog
* Thu Aug 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.2.1-1
- Fix FTBFS
- Update to latest upstream release 5.2.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 5.1.2-1
- Update to 5.1.2 upstream relase

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 5.1.1-1
- Update to upstream 5.1.1 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Piotr Popieluch <piotr1212@gmail.com> - 5.0.1-1
- Initial package
