%global gem_name logstash-event

Name:           rubygem-%{gem_name}
Version:        1.2.02
Release:        11%{?dist}
Summary:        Library that contains the classes required to create LogStash events

License:        ASL 2.0
URL:            https://github.com/logstash/logstash
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch
BuildRequires:  rubygems-devel
# for tests:
# BuildRequires: rubygem(rspec)
# BuildRequires: rubygem(insist) = 1.0.0
# missing in gemspec
Requires:       rubygem(json)
%if 0%{?fedora} && 0%{?fedora} <= 20 || 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
rubygem-%{gem_name} contains the classes required to create LogStash events
(combination of timestamp in ISO8601 format and message in any format) and their
serialization to json.

%{gem_name} rubygem is part of LogStash project, http://logstash.net/.


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
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Dependencies for test suite not in Fedora/EPEL yet
#%%check
#pushd .%%{gem_instdir}
#rspec -Ilib spec/event.rb
#popd


%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 František Dvořák <valtri@civ.zcu.cz> - 1.2.02-2
- More elaborate description
- Added explicit require on json rubygem

* Wed Aug 20 2014 František Dvořák <valtri@civ.zcu.cz> - 1.2.02-1
- Initial package
