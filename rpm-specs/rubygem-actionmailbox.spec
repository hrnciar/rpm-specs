%global gem_name actionmailbox

Name: rubygem-%{gem_name}

Version: 6.0.3.4
Release: 1%{?dist}
Summary: Inbound email handling framework
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# Actionmailbox gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/actionmailbox && git archive -v -o actionmailbox-6.0.3.4-tests.txz v6.0.3.4 test/
Source1: actionmailbox-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may get them like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-6.0.3.4-tools.txz v6.0.3.4 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(activestorage) = %{version}
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(webmock)
BuildArch: noarch

%description
Receive and process incoming emails in Rails applications.


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
pushd .%{gem_instdir}/
ln -s %{_builddir}/tools ..
cp -a %{_builddir}/test .

export BUNDLE_GEMFILE=${PWD}/../Gemfile

cat > $BUNDLE_GEMFILE <<EOF
gem "railties"
gem "actionmailer"
gem "activestorage"
gem "sprockets-rails"
gem "sqlite3"
gem "webmock"
EOF

# Remove byebug dependency
sed -i '/^require..byebug./ s/^/#/' test/test_helper.rb

ruby -rbundler -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Oct  8 12:00:49 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to actionmailbox 6.0.3.4.
  Resolves: rhbz#1877507

* Tue Sep 22 01:15:13 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to actionmailbox 6.0.3.3.
  Resolves: rhbz#1877507

* Mon Aug 17 05:14:02 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to actionmailbox 6.0.3.2.

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Initial package: ActionMailbox 6.0.3.1.
