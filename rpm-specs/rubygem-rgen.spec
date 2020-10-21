%global gem_name rgen

Name: rubygem-%{gem_name}
Version: 0.8.4
Release: 4%{?dist}
Summary: Ruby Modelling and Generator Framework
License: MIT
URL: https://github.com/mthiede/rgen
Source0:  https://github.com/mthiede/rgen/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
# Upstream commit that fixes tests failures
Patch0: 1124f4303db52973967e78d93512a1c1b64f23cf.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
RGen is a framework for Model Driven Software Development (MDSD) in Ruby. This
means that it helps you build Metamodels, instantiate Models, modify and
transform Models and finally generate arbitrary textual content from it.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}
%patch0 -p1
sed -i '/abort/d'   %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec
# Disable doc as it fails otherwise it's identical to gem_install macro
CONFIGURE_ARGS="--with-cflags='%{optflags}' --with-cxxflags='%{optflags}' $CONFIGURE_ARGS" \
gem install \
        -V -N \
        --local \
        --build-root . \
        --force \
        %{gem_name}-%{version}%{?prerelease}.gem

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Fix line endings.
sed -i 's:\r::' %{buildroot}%{gem_instdir}/CHANGELOG

%check
pushd .%{gem_instdir}
RUBYOPT=-rrubygems ruby test/rgen_test.rb ||:
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
#%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/Project.yaml
%{gem_instdir}/test
%{gem_instdir}/Rakefile

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 26 2019 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.4-1
- Upstream 0.8.4
- Disable documentation build

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.7.0-7
- Adjust for ruby 2.5 (RUBY_INTEGER_UNIFICATION from 2.4, and
  bigdecimal split, ubygems deprecation)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Vít Ondruch <vondruch@redhat.com> - 0.7.0-1
- Update to RGen 0.7.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Sam Kottler <shk@redhat.com> - 0.6.6-2
- Fixes based on review feedback

* Mon Jan 06 2014 Sam Kottler <shk@redhat.com> - 0.6.6-1
- Initial package
