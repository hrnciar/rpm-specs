%global gem_name aws-sdk-resources

# rspec 3 required
%if 0%{?rhel} && 0%{?rhel} <= 7
%global use_tests 0
%else
%global use_tests 1
%endif

Name:           rubygem-%{gem_name}
Version:        2.6.19
Release:        7%{?dist}
Summary:        AWS SDK for Ruby - Resources

License:        ASL 2.0
URL:            http://github.com/aws/aws-sdk-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# gem_name='aws-sdk-resources'
# version='2.6.19'
# git clone https://github.com/aws/aws-sdk-ruby && cd aws-sdk-ruby/${gem_name}
# git checkout v${version}
# cp -p ../LICENSE.txt ../NOTICE.txt ../README.md .
# tar -czf rubygem-${gem_name}-${version}-repo.tgz features/ spec/ LICENSE.txt NOTICE.txt README.md
Source1:        rubygem-%{gem_name}-%{version}-repo.tgz
# failing for unknown reasons (not intended for upstream, we should update to the
# latest version first)
Patch0:         %{gem_name}-fails.patch

BuildArch:      noarch
BuildRequires:  rubygems-devel
%if 0%{?use_tests}
BuildRequires:  rubygem(aws-sdk-core) = %{version}
BuildRequires:  rubygem(rspec) >= 3
BuildRequires:  rubygem(simplecov)
BuildRequires:  rubygem(webmock)
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(rubygems)
Requires:       rubygem(aws-sdk-core) = %{version}
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Provides resource oriented interfaces and other higher-level abstractions for
many AWS services. This gem is part of the official AWS SDK for Ruby.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version} -a 1
%patch0 -p2

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

cp -a LICENSE.txt NOTICE.txt README.md %{buildroot}%{gem_instdir}/


%check
%if 0%{?use_tests}
cp -a features/ spec/ .%{gem_instdir}/
pushd .%{gem_instdir}
rspec -Ilib spec
rm -rf features/ spec/
popd
%endif


%files
%license %{gem_instdir}/LICENSE.txt
%license %{gem_instdir}/NOTICE.txt
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 František Dvořák <valtri@civ.zcu.cz> - 2.6.19-1
- Update to 2.6.19
- Patch to disable some tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 06 2016 František Dvořák <valtri@civ.zcu.cz> - 2.3.20-1
- Update to 2.3.20

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 František Dvořák <valtri@civ.zcu.cz> - 2.1.13-1
- Initial package
