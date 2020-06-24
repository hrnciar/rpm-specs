# Generated from apipie-rails-0.0.13.gem by gem2rpm -*- rpm-spec -*-
%global gem_name apipie-rails

Name: rubygem-%{gem_name}
Version: 0.5.5
Release: 6%{?dist}
Summary: Rails REST API documentation tool
# The project itself is MIT
# For ASL 2.0, see https://github.com/Apipie/apipie-rails/issues/66
# (bundled JS files under app/public)
License: MIT and ASL 2.0
URL: http://github.com/Apipie/apipie-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# TODO: https://lists.fedoraproject.org/pipermail/packaging/2015-July/010794.html
Requires: js-jquery1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/rspec
BuildRequires: rubygem(actionmailer)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(rails-controller-testing)
BuildRequires: rubygem(rspec-rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: web-assets-devel
BuildArch: noarch

%description
Apipie-rails is a DSL and Rails engine for documenting your RESTful API.
Instead of traditional use of #comments, Apipie lets you describe the code,
through the code. This brings advantages like:

* No need to learn yet another syntax, you already know Ruby, right?
* Possibility of reusing the docs for other purposes (such as validation)
* Easier to extend and maintain (no string parsing involved)
* Possibility of reusing other sources for documentation purposes (such as
  routes etc.)

The documentation is available from within your app (by default under the
/apipie path.) In development mode, you can see the changes as you go. It's
markup language agnostic, and even provides an API for reusing the
documentation data in JSON.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}

# Replace bundled jQuery by link to system version.
ln -sf %{_jsdir}/jquery/1/jquery.js app/public/apipie/javascripts/bundled/jquery.js
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove empty .gitkeep files, that rpmlint complains about, we don't need
# them in RPMs.
find %{buildroot}%{gem_instdir}/spec -type f -name '.gitkeep' -exec rm {} \;

# This has deprecated /bin/env shebang, but since it appears to be dead
# code, just remove it.
# https://github.com/Apipie/apipie-rails/issues/135
rm %{buildroot}%{gem_libdir}/apipie/client/generator.rb
rm -r %{buildroot}%{gem_libdir}/apipie/client

%check
pushd .%{gem_instdir}
# Don't use Bundler.
rm Gemfile*
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler.require/ s/^/#/" spec/dummy/config/application.rb

rspec -rrails-controller-testing spec
popd


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/APACHE-LICENSE-2.0
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_libdir}
# exclude useless rel-eng directory
%exclude %{gem_instdir}/rel-eng
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile*
%doc %{gem_instdir}/README.rst
%doc %{gem_instdir}/NOTICE
%{gem_instdir}/Rakefile
%{gem_instdir}/apipie-rails.gemspec
%{gem_instdir}/images
%{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1
- Update to apipie-rails 0.5.5.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Dominic Cleal <dominic@cleal.org> - 0.5.1-1
- Update to apipie-rails 0.5.1.

* Mon Feb 20 2017 Vít Ondruch <vondruch@redhat.com> - 0.4.0-1
- Update to apipie-rails 0.4.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 01 2016 Jun Aruga <jaruga@redhat.com> - 0.3.6-1
- Update version to 0.3.6 to test suite for Ruby 2.3 compatibility.
  (rhbz#1308005)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Vít Ondruch <vondruch@redhat.com> - 0.3.4-1
- Update to apipie-rails 0.3.4.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.22-1
- Update to apipie-rails 0.0.22.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.21-1
- Update to apipie-rails 0.0.21.

* Thu Mar 28 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.13-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.0.13-2
- Fixed some file permission issues.
- Keep the specs in -doc subpackage.
- Run the tests without git.
- Add runtime dependency on rubygem(rails).

* Tue Nov 20 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.0.13-1
- Initial package
