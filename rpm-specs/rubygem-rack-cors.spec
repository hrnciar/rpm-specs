%global gem_name rack-cors

Name:           rubygem-%{gem_name}
Version:        1.1.1
Release:        3%{?dist}
Summary:        Middleware for enabling Cross-Origin Resource Sharing in Rack apps

License:        MIT
URL:            https://github.com/cyu/rack-cors
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(minitest) >= 5.11.0
BuildRequires:  rubygem(mocha) >= 1.6.0
BuildRequires:  rubygem(rack-test)

%description
Middleware that will make Rack-based apps CORS compatible.

Fork the project here: https://github.com/cyu/rack-cors.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ruby -rminitest/autorun -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/test/
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 František Dvořák <valtri@civ.zcu.cz> - 1.1.1-1
- Update to 1.1.1 (#1692223)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 František Dvořák <valtri@civ.zcu.cz> - 1.0.2-1
- Update to 1.0.2 (#1505204)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 František Dvořák <valtri@civ.zcu.cz> - 1.0.1-1
- Update to 1.0.1 (#1471444)

* Tue Feb 21 2017 František Dvořák <valtri@civ.zcu.cz> - 0.4.1-1
- Update to 0.4.1 (#1418491)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 František Dvořák <valtri@civ.zcu.cz> - 0.4.0-1
- Update to 0.4.0 (#1212051)

* Sun Jan 04 2015 František Dvořák <valtri@civ.zcu.cz> - 0.3.1-1
- Update to 0.3.1

* Tue Dec 23 2014 František Dvořák <valtri@civ.zcu.cz> - 0.3.0-1
- Update to 0.3.0
- Update file list
- Cleanups

* Fri Oct 10 2014 František Dvořák <valtri@civ.zcu.cz> - 0.2.9-1
- Initial package
