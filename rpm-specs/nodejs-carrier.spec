%global shortname carrier

Name:           nodejs-carrier
Version:        0.3.0
Release:        1%{?dist}
Summary:        Evented stream line reader for node.js

License:        MIT
URL:            https://github.com/pgte/%{shortname}

Source0:        http://registry.npmjs.org/%{shortname}/-/%{shortname}-%{version}.tgz
# Created by running the below command in the unpacked %%{SOURCE0}
# $ npm install --save-dev && tar -czf ../%%{shortname}-%%{version}-node_modules.tar.gz node_modules
Source1:        %{shortname}-%{version}-node_modules.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging nodejs(engine)

%description
%{shortname} helps you implement new-line terminated protocols over node.js.
The client can send you chunks of lines and carrier will only notify you on
each completed line

%prep
%setup -qn package

# Extract cached development dependencies
tar -xzf '%{SOURCE1}'

%build
# Nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{shortname}/
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/%{shortname}

%check
for test in $(ls test/); do
    %{__nodejs} test/${test}
done

%files
%{nodejs_sitelib}/%{shortname}
%doc README.markdown
%license LICENSE


%changelog
* Mon Aug 17 2020 Jan Staněk <jstanek@redhat.com> - 0.3.0-1
- Upgrade to version 0.3.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 07 2015 Gerard Ryan <galileo@fedoraproject.org> - 0.1.14-1
- Initial package
