Name:           nodejs-async-queue
Version:        0.1.0
Release:        10%{?dist}
Summary:        Simple FIFO queue to execute async functions linear

License:        MIT or BSD
URL:            https://github.com/martinj/node-async-queue
Source0:        https://registry.npmjs.org/async-queue/-/async-queue-%{version}.tgz
# https://github.com/martinj/node-async-queue/pull/1
Patch0:         nodejs-async-queue-license.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(should)


%description
%{summary}.


%prep
%setup -q -n package
%patch0 -p1
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/async-queue
cp -pr package.json async-queue.js %{buildroot}%{nodejs_sitelib}/async-queue
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha test/*.test.js


%files
%doc README.md
%license MIT-LICENSE BSD-LICENSE
%{nodejs_sitelib}/async-queue


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep  4 2015 Tom Hughes <tom@compton.nu> - 0.1.0-2
- Correct licensing

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Initial build of 0.1.0
