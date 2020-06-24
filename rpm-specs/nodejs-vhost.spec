%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-vhost
Version:    3.0.2
Release:    7%{?dist}
Summary:    Virtual domain hosting middleware for Node.js and Connect
License:    MIT
URL:        https://github.com/expressjs/vhost
Source0:    https://github.com/expressjs/vhost/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  mocha
#BuildRequires:  npm(connect)
#BuildRequires:  npm(should)
BuildRequires:  npm(supertest)
%endif

%description
%{summary}.


%prep
%autosetup -n vhost-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vhost
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/vhost

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

%if 0%{?enable_tests}
mocha --reporter spec --check-leaks test/
%endif


%files
%doc README.md HISTORY.md
%license LICENSE
%{nodejs_sitelib}/vhost


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- initial package
