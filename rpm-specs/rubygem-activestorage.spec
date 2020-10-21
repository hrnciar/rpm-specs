# Generated from activestorage-0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activestorage

# Circular dependency with rubygem-railties.
%bcond_with bootstrap

# FFmpeg can be used in tests, but is not available in Fedora
%bcond_with ffmpeg

Name: rubygem-%{gem_name}
Version: 6.0.3.4
Release: 1%{?dist}
Summary: Local and cloud file storage framework
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# The gem doesn't ship with the test suite.
# You may check it out like so
# git clone https://github.com/rails/rails.git
# cd rails/activestorage && git archive -v -o activestorage-6.0.3.4-tests.txz v6.0.3.4 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may check it out like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-6.0.3.4-tools.txz v6.0.3.4 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activejob) = %{version}
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(rails) = %{version}
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(image_processing)
BuildRequires: rubygem(sqlite3)
# FFmpeg is not available in Fedora
%{?with_ffmpeg:BuildRequires: %{_bindir}/ffmpeg}
BuildRequires: %{_bindir}/mutool
BuildRequires: %{_bindir}/pdftoppm
%endif
# Used for creating file previews
Suggests: %{_bindir}/mutool
Suggests: %{_bindir}/pdftoppm
Suggests: %{_bindir}/ffmpeg

BuildArch: noarch

%description
Attach cloud and local files in Rails applications.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if %{without bootstrap}
# fake RAILS_FRAMEWORK_ROOT
ln -s %{gem_dir}/specifications/rails-%{version}%{?prerelease}.gemspec .%{gem_dir}/gems/rails.gemspec
ln -s %{gem_dir}/gems/railties-%{version}%{?prerelease}/ .%{gem_dir}/gems/railties
ln -s %{gem_dir}/gems/activerecord-%{version}%{?prerelease}/ .%{gem_dir}/gems/activerecord
ln -s %{gem_dir}/gems/activejob-%{version}%{?prerelease}/ .%{gem_dir}/gems/activejob
ln -s %{gem_dir}/gems/actionpack-%{version}%{?prerelease}/ .%{gem_dir}/gems/actionpack
ln -s %{gem_dir}/gems/activesupport-%{version}%{?prerelease}/ .%{gem_dir}/gems/activesupport
ln -s ${PWD}%{gem_instdir} .%{gem_dir}/gems/%{gem_name}

pushd .%{gem_dir}/gems/%{gem_name}
ln -s %{_builddir}/tools ..
# Copy the tests into place.
cp -a %{_builddir}/test .

touch Gemfile
echo 'gem "actionpack"' >> ../Gemfile
echo 'gem "activerecord"' >> ../Gemfile
echo 'gem "activejob"' >> ../Gemfile
echo 'gem "sprockets-rails"' >> ../Gemfile
echo 'gem "image_processing"' >> ../Gemfile
echo 'gem "rails"' >> ../Gemfile
echo 'gem "sqlite3"' >> ../Gemfile

# Disable tests that require FFmpeg
%if %{without ffmpeg}
mv test/analyzer/video_analyzer_test.rb{,.disable}
for f in \
  models/preview \
  models/representation \
  previewer/video_previewer
do
sed -i '/^  test ".* an MP4 video" do$/,/^  end$/ s/^/#/g' \
  test/${f}_test.rb
done
%endif

export RUBYOPT="-I${PWD}/../%{gem_name}/lib"
export PATH="${PWD}/../%{gem_name}/exe:$PATH"
export BUNDLE_GEMFILE=${PWD}/../Gemfile

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Oct  8 11:56:48 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to activestorage 6.0.3.4.
  Resolves: rhbz#1877544

* Tue Sep 22 01:10:44 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to activestorage 6.0.3.3.
  Resolves: rhbz#1877544

* Mon Aug 17 05:23:03 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to activestorage 6.0.3.2.
  Resolves: rhbz#1742796

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Update to ActiveStorage 6.0.3.1.
  Resolves: rhbz#1742796

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Tom Callaway <spot@fedoraproject.org> - 5.2.3-4
- rebuild for new rubygem-connection_pool

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-2
- Enable tests.

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-1
- Update to Active Storage 5.2.3.

* Mon Mar 18 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-2
- Enable tests.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-1
- Update to Active Storage 5.2.2.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 5.2.2-2
- Update to Active Storage 5.2.2.

* Thu Aug 09 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-2
- Enable tests.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-1
- Update to Active Storage 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-2
- Enable tests.

* Wed May 02 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to Active Storage 5.2.0.
- Moved to Rails repository.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Vít Ondruch <vondruch@redhat.com> - 0.1-1
- Initial package
