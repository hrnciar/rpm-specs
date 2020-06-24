%global gem_name rake-contrib

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 8%{?dist}
Summary: Additional libraries for Rake
License: MIT
URL: https://github.com/ruby/rake-contrib
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ruby/rake-contrib.git
# HEAD = a587db7f45dc1d24c7c
# cd rake-contrib; tar -czf rake-contrib-tests.tar.gz test
Source1: %{gem_name}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rake)
BuildRequires: ruby
BuildArch: noarch

%description
Additional libraries for Rake.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

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

tar -xzf %{SOURCE1}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rake-contrib.gemspec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-2
- Add test suite

* Sat Feb 04 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-1
- Initial package
