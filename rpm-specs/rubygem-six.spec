# Generated from six-0.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name six

Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 13%{?dist}
Summary: Ultra simple authorization gem for ruby
License: MIT 
URL: https://github.com/randx/six
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/randx/six.git && cd six
# git checkout v0.2.0
# tar cf rubygem-six-0.2.0-specs.tar.xz spec/
Source1: %{name}-%{version}-specs.tar.xz
# https://github.com/randx/six/pull/10
Source2: https://github.com/randx/six/blob/master/LICENSE 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) < 3.0
BuildArch: noarch

%description
Ultra lite authorization library.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -a 1 -T -n %{gem_name}-%{version}
cp  -p %{SOURCE2} .  
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite
%check
cp -pr spec/ .%{gem_instdir}
pushd .%{gem_instdir}
  sed -i -e "/require \"bundler\"/ s/^/#/" -e "/[Bb]undler/ s/^/#/" spec/spec_helper.rb
  rspec2 -Ilib spec
popd

%files
%dir %{gem_instdir}
%license LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 4 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.2.0-4
- add link to pull request with license 

* Mon Aug 3 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.2.0-3
- add license file

* Mon Aug 3 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.2.0-2
- changed description
- changed summary
- add rubygem(rspec) to BRs

* Sun Jul 19 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.2.0-1
- Initial package
