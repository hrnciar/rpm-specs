%global gem_name macaddr

Name:           rubygem-%{gem_name}
Version:        1.7.2
Release:        2%{?dist}
Summary:        MAC Address Determination for Ruby

License:        Ruby or BSD
URL:            https://github.com/ahoward/macaddr
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# full license text not in the sources
# https://github.com/ahoward/macaddr/issues/27
Source1:        https://raw.githubusercontent.com/ruby/ruby/trunk/COPYING
Source2:        https://raw.githubusercontent.com/ruby/ruby/trunk/BSDL

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(systemu) >= 2.6.5
BuildRequires:  rubygem(systemu) < 2.7
BuildRequires:  rubygem(test-unit)
%if 0%{?fedora} && 0%{?fedora} <= 20 || 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(systemu) >= 2.6.5
Requires:       rubygem(systemu) < 2.7
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Cross platform mac address determination for Ruby.


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

cp -p %{SOURCE1} %{SOURCE2} %{buildroot}%{gem_instdir}/


%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}/
%doc %{gem_instdir}/LICENSE
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/BSDL
%{gem_libdir}/
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/test/
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/rvmrc.example
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/README


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 František Dvořák <valtri@civ.zcu.cz> - 1.7.2-1
- Update to 1.7.2 (#1717646)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 08 2015 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-2
- Update for F22, proper BR for test/unit

* Mon Dec 29 2014 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-1
- Initial package
