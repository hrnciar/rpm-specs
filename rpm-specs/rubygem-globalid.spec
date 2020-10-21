# Generated from globalid-0.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name globalid

%{?_with_bootstrap: %global bootstrap 1}

Name: rubygem-%{gem_name}
Version: 0.4.2
Release: 4%{?dist}
Summary: Refer to any model with a URI: gid://app/class/id
License: MIT
URL: http://www.rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/globalid.git && cd globalid
# git checkout v0.4.2
# tar czvf globalid-0.4.2-tests.tar.gz test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
%if ! 0%{?bootstrap}
BuildRequires: rubygem(activesupport) >= 4.1
BuildRequires: rubygem(activemodel) >= 4.1
BuildRequires: rubygem(railties) >= 4.1
%endif
BuildArch: noarch

%description
URIs for your models makes it easy to pass references around.


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


%if ! 0%{?bootstrap}
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# Avoid Bundler dependency.
sed -i "/bundler\/setup/ s/^/#/" ./test/helper.rb

# The skipped test case is probably going to be "fixed" by:
# https://github.com/rails/globalid/pull/107
sed -i "/defaults to nil when secret_token is not present' do/a \\
    skip 'Not compatible with Rails 5.2'" test/cases/railtie_test.rb

ruby -Ilib:test -rforwardable -e "Dir.glob './test/cases/*test.rb', &method(:require)"
popd
%endif


%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Pavel Valena <pvalena@redhat.com> - 0.4.2-1
- Update to globalid 0.4.2.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Vít Ondruch <vondruch@redhat.com> - 0.4.1-1
- Disable Rails 5.2 incompatible test case.
- Modernize the .spec file a bit.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 0.4.1-1
- Update to 0.4.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jun Aruga <jaruga@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Tue Feb 14 2017 Jun Aruga <jaruga@redhat.com> - 0.3.6-3
- Fix Fixnum/Bignum deprecated warning for Ruby 2.4.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 07 2016 Jun Aruga <jaruga@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Josef Stribny <jstribny@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Tue Jan 06 2015 Josef Stribny <jstribny@redhat.com> - 0.3.0-1
- Initial package
