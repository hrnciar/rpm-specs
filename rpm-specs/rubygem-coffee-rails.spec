# Generated from coffee-rails-3.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-rails

Name: rubygem-%{gem_name}
Version: 5.0.0
Release: 1%{?dist}
Summary: Coffee Script adapter for the Rails asset pipeline
License: MIT
URL: https://github.com/rails/coffee-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/coffee-rails.git && cd coffee-rails
# git archive -v -o coffee-rails-5.0.0-tests.tar.gz v5.0.0 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(coffee-script) >= 2.2.0
BuildRequires: rubygem(railties) => 4.0.0
BuildRequires: rubygem(sprockets-rails)
BuildRequires: %{_bindir}/node
BuildArch: noarch

%description
Coffee Script adapter for the Rails asset pipeline.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# Disable Bundler.
sed -i '/require .bundler\/setup./ s/^/#/' test/test_helper.rb

ruby -I.:test:lib -e 'Dir.glob("test/**/*_test.rb").each {|t| require t}'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sat Aug 22 00:18:44 GMT 2020 Pavel Valena <pvalena@redhat.com> - 5.0.0-1
- Update to coffee-rails 5.0.0.
  Resolves: rhbz#1702437

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Jun Aruga <jaruga@redhat.com> - 4.2.2-1
- Update to coffee-rails 4.2.2, aliging an output of gem2rpm.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Jun Aruga <jaruga@redhat.com> - 4.2.1-1
- Fix for FTBFS. (rhbz#1357056)
- Update to coffee-rails 4.2.1.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Josef Stribny <jstribny@redhat.com> - 4.1.0-1
- Update to 4.1.0

* Wed Jun 25 2014 Vít Ondruch <vondruch@redhat.com> - 4.0.1-1
- Update to coffee-rails 4.0.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to coffee-rails 4.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.2-1
- Initial package
