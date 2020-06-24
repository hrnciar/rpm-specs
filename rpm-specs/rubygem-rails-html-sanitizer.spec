# Generated from rails-html-sanitizer-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rails-html-sanitizer

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 2%{?dist}
Summary: This gem is responsible to sanitize HTML fragments in Rails applications
License: MIT
URL: https://github.com/rails/rails-html-sanitizer
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(loofah)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rails-dom-testing)
BuildArch: noarch

%description
HTML sanitization for Rails applications.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
# Some tests are failing, upstream issue
# https://github.com/rails/rails-html-sanitizer/issues/99
for name in uri_escaping_of_{{name,href,src}_attr,name_action}_in_a_tag_in_safe_list_sanitizer; do
sed -i "/^  def test_${name}$/ a \    skip" \
  test/sanitizer_test.rb
done

ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
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
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Pavel Valena <pvalena@redhat.com> - 1.3.0-1
- Update to rails-html-sanitizer 1.3.0.

* Wed Sep 18 2019 Pavel Valena <pvalena@redhat.com> - 1.2.0-1
- Update to rails-html-sanitizer 1.2.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Vít Ondruch <vondruch@redhat.com> - 1.0.4-1
- Update to rails-html-sanitizer 1.0.4.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Jun Aruga <jaruga@redhat.com> - 1.0.3-3
- Improve tests.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 1.0.3-1
- Update to 1.0.3
- License file is missing https://github.com/rails/rails-html-sanitizer/pull/47
- Skip failing tests due to possible incompatibility with libxml2

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 Vít Ondruch <vondruch@redhat.com> - 1.0.1-1
- Initial package
