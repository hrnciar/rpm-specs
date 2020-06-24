%{?nodejs_find_provides_and_requires}

# Disabled as npm(chunky) is not available yet
%global enable_tests 0

Name:           nodejs-pg-packet-stream
Version:        1.1.0
Release:        2%{?dist}
Summary:        Packet stream reader for Postgres

License:        MIT
URL:            https://www.npmjs.com/package/pg-packet-stream
Source0:        https://registry.npmjs.org/pg-packet-stream/-/pg-packet-stream-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(chai)
BuildRequires:  npm(chunky)
BuildRequires:  npm(mocha)
%endif


%description
%{summary}.


%prep
%autosetup -n package
chmod a-x LICENSE
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-packet-stream
install -p -m644 package.json %{buildroot}%{nodejs_sitelib}/pg-packet-stream
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-packet-stream/dist
install -p -m644 dist/index.js dist/messages.js dist/BufferReader.js %{buildroot}%{nodejs_sitelib}/pg-packet-stream/dist
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{nodejs_sitelib}/mocha/bin/mocha dist/**/*.test.js
%endif

%files
%license LICENSE
%{nodejs_sitelib}/pg-packet-stream


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Initial build of 1.1.0.
