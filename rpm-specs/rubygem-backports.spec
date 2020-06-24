# Generated from backports-2.5.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name backports

Name: rubygem-%{gem_name}
Version: 3.17.1
Release: 1%{?dist}
Summary: Backports of Ruby features for older Ruby
License: MIT
URL: http://github.com/marcandre/backports
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/marcandre/backports.git && cd backports
# git archive -v -o backports-3.17.1-tests.tar.gz v3.17.1 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
Essential backports that enable many of the nice features of Ruby for earlier
versions.


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
# Move the tests into place
ln -s %{_builddir}/test test

# TODO: More test could be enabled, if MSpec and RubySpec are available
# in Fedora.

ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/backports.gemspec

%changelog
* Fri Apr 24 2020 Vít Ondruch <vondruch@redhat.com> - 3.17.1-1
- Update to backports 3.17.1.
  Resolves: rhbz#1679034
  Resolves: rhbz#1799992

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Pavel Valena <pvalena@redhat.com> - 3.11.4-1
- Update to backports 3.11.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Vít Ondruch <vondruch@redhat.com> - 3.11.0-1
- Update to backports 3.11.0.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Vít Ondruch <vondruch@redhat.com> - 3.7.0-1
- Update to backports 3.7.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Vít Ondruch <vondruch@redhat.com> - 3.6.4-1
- Update to backports 3.6.4.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Vít Ondruch <vondruch@redhat.com> - 3.6.0-1
- Update to backports 3.6.0.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 17 2013 Vít Ondruch <vondruch@redhat.com> - 3.3.4-1
- Update to backports 3.3.4.

* Mon Sep 02 2013 Vít Ondruch <vondruch@redhat.com> - 3.3.3-1
- Update to backports 3.3.3.

* Mon Apr 30 2012 Vít Ondruch <vondruch@redhat.com> - 2.5.1-2
- Fixed license.

* Fri Apr 27 2012 Vít Ondruch <vondruch@redhat.com> - 2.5.1-1
- Initial package
