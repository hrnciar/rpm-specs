%{?nodejs_find_provides_and_requires}

Name:       nodejs-jsonparse
Version:    1.2.0
Release:    8%{?dist}
Summary:    Pure-js JSON streaming parser for node.js
License:    MIT
URL:        https://github.com/creationix/jsonparse
Source:     http://registry.npmjs.org/jsonparse/-/jsonparse-%{version}.tgz


BuildArch:  noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(tap)
BuildRequires:  npm(tape)

ExclusiveArch: %{nodejs_arches} noarch

%description
This is a streaming JSON parser for Node.js



%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jsonparse
cp -pr jsonparse.js package.json \
    %{buildroot}%{nodejs_sitelib}/jsonparse



%check
%nodejs_symlink_deps --check
/usr/bin/tap  test/*.js

%files
%doc LICENSE README.markdown examples/
%{nodejs_sitelib}/jsonparse



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Anish Patil <anish.developer@gmail.com> - 1.2.0-1
- Upstream has released new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 Anish Patil <apatil@redhat.com> - 1.0.0-1
- Upstream has released new version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Anish Patil <apatil@redhat.com> - 0.0.6-4
- Incorporated package review comments

* Wed May 28 2014 Anish Patil <apatil@redhat.com> - 0.0.6-3
- Incorporated package review comments

* Wed May 7 2014 Anish Patil <apatil@redhat.com> - 0.0.6-2
- Incorporated package review comments

* Thu Apr 10 2014 Anish Patil <apatil@redhat.com> - 0.0.6-1
- Initial package
