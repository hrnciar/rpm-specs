%{?nodejs_find_provides_and_requires}

Name:       nodejs-static-favicon
Version:    1.0.2
Release:    11%{?dist}
Summary:    Favicon serving middleware with caching for Node.js and Connect
License:    MIT
URL:        https://github.com/expressjs/favicon
Source0:    http://registry.npmjs.org/static-favicon/-/static-favicon-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/static-favicon
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/static-favicon

mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -D -m0644 favicon.ico \
    %{buildroot}%{_datadir}/%{name}/favicon.ico
ln -sf %{_datadir}/%{name}/favicon.ico \
    %{buildroot}%{nodejs_sitelib}/static-favicon/favicon.ico

%nodejs_symlink_deps


%files
%doc LICENSE README.md
%{nodejs_sitelib}/static-favicon
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/favicon.ico


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.2-1
- update to upstream release 1.0.2

* Sat Mar 15 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.1-1
- update to upstream release 1.0.1

* Tue Mar 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-2
- own {_datadir}/{name} directory

* Mon Mar 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- initial package
