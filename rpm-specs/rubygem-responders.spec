%global gem_name responders

Name:           rubygem-%{gem_name}
Version:        2.4.0
Release:        8%{?dist}
Summary:        Set of Rails responders to dry up your application

License:        MIT
URL:            http://github.com/plataformatec/responders
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone http://github.com/plataformatec/responders && cd responders
# git checkout v2.4.0
# tar -czf rubygem-responders-2.4.0-test.tgz test/
Source1:        %{name}-%{version}-test.tgz

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(activemodel)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(rails)
BuildRequires:  rubygem(rails-controller-testing)

%description
A set of Rails responders to dry up your application.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version} -a 1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
cp -a test/ ./%{gem_instdir}
pushd .%{gem_instdir}
sed -i -e '\,bundler/setup,d' test/test_helper.rb
ruby -Ilib:test test/**/*_test.rb
rm -rf test/
popd


%files
%dir %{gem_instdir}/
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 František Dvořák <valtri@civ.zcu.cz> - 2.4.0-1
- Update to 2.4.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 František Dvořák <valtri@civ.zcu.cz> - 2.2.0-1
- Update to 2.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 František Dvořák <valtri@civ.zcu.cz> - 2.1.0-3
- Patch to update tests with rails 4.2.1
- Workaround jruby

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 František Dvořák <valtri@civ.zcu.cz> - 2.1.0-1
- Initial package
