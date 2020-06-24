%{?nodejs_find_provides_and_requires}

Name:       nodejs-jsonstream
Version:    1.3.1
Release:    7%{?dist}
Summary:    Streaming JSON.parse and stringify for Node.js
License:    MIT or ASL 2.0
URL:        http://github.com/dominictarr/JSONStream
Source:     http://registry.npmjs.org/JSONStream/-/JSONStream-%{version}.tgz



BuildArch:  noarch

BuildRequires:  nodejs-packaging


%description
Streaming JSON.parse and stringify for Node.js


%prep
%setup -q -n package
%setup -T -D  -q -n package
%nodejs_fixdep jsonparse > '~0.0.5'
%nodejs_fixdep through > '~2.2.7'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/JSONStream
cp -p package.json index.js %{buildroot}%{nodejs_sitelib}/JSONStream


%files
%doc readme.markdown LICENSE.MIT LICENSE.APACHE2 examples/
%{nodejs_sitelib}/JSONStream


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 06 2017 Jared Smith <jsmith@fedoraproject.org> - 1.3.1-1
- Update to upstream 1.3.1 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Anish Patil <anish.developer@gmail.com> - 1.0.3-1
- Upstream has released new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 08 2014 Anish Patil <apatil@redhat.com> - 0.10.0-2
- Initial package and incorporated package review comments

* Mon Dec 08 2014 Anish Patil <apatil@redhat.com> - 0.10.0-1
- Initial package and incorporated package review comments

* Thu Apr 10 2014 Anish Patil <apatil@redhat.com> - 0.8.0-1
- initial package
