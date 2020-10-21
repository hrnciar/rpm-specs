%global gem_name aws-sigv4

Name:           rubygem-%{gem_name}
Version:        1.0.2
Release:        7%{?dist}
Summary:        AWS Signature Version 4 library

License:        ASL 2.0
URL:            http://github.com/aws/aws-sdk-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone http://github.com/aws/aws-sdk-ruby aws-sdk-ruby; cd aws-sdk-ruby
# id=d6b12f0853633f00e6be5dcc9dbfda9d8676f39a
# git checkout $id
# cp -vp LICENSE.txt NOTICE.txt gems/aws-sigv4/
# (cd gems/aws-sigv4; tar -czf ../../rubygem-aws-sigv4-1.0.2-repo.tgz spec/ *.txt)
Source1:        %{name}-%{version}-repo.tgz

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}-%{release}
%endif

%description
Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version}
tar -xzf %{SOURCE1}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
cp -pr spec/ ./%{gem_instdir}
pushd ./%{gem_instdir}
rspec -Ilib spec
rm -rf spec
popd


%files
%license LICENSE.txt NOTICE.txt
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 František Dvořák <valtri@civ.zcu.cz> - 1.0.2-1
- Initial package
