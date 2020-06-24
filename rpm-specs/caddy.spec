%bcond_with bootstrap

%if %{without bootstrap}
%bcond_without check
# http plugins
%bcond_without geoip
%bcond_without realip
# dns plugins
%bcond_without azure
%bcond_without cloudflare
%bcond_without digitalocean
%bcond_without googlecloud
%bcond_without pdns
%bcond_without rackspace
%bcond_without route53
%endif

# https://github.com/caddyserver/caddy
%global goipath         github.com/caddyserver/caddy
%global goaltipaths     github.com/mholt/caddy
Version:                1.0.3

%gometa

%global common_description %{expand:
Caddy is the HTTP/2 web server with automatic HTTPS.}

%global golicenses      LICENSE.txt
%global godocs          dist/README.txt dist/CHANGES.txt

# added in F32, remove in F34
%global godevelheader %{expand:
Obsoletes:      golang-github-mholt-caddy-devel < 1.0.0-3
}

Name:           caddy
Release:        3%{?dist}
Summary:        HTTP/2 web server with automatic HTTPS
License:        ASL 2.0
URL:            https://caddyserver.com
Source0:        %{gosource}
Source1:        caddy.conf
Source2:        caddy.service
Source3:        index.html
# https://github.com/caddyserver/caddy/issues/2584
Patch0:         enable-appVersion-ldflag.patch
# https://github.com/caddyserver/caddy/pull/2728
Patch1:         use-gopkgin-blackfriday-import-path.patch

# https://github.com/mholt/caddy/commit/80dfb8b2a7f89b120a627bc4d866a1dc5ed3d92f#diff-04c6e90faac2675aa89e2176d2eec7d8
BuildRequires:  golang >= 1.12
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/flynn/go-shlex)
BuildRequires:  golang(github.com/go-acme/lego/certcrypto)
BuildRequires:  golang(github.com/go-acme/lego/challenge)
BuildRequires:  golang(github.com/go-acme/lego/challenge/tlsalpn01)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/hashicorp/go-syslog)
BuildRequires:  golang(github.com/jimstudt/http-authentication/basic)
BuildRequires:  golang(github.com/klauspost/cpuid)
BuildRequires:  golang(github.com/lucas-clemente/quic-go)
BuildRequires:  golang(github.com/lucas-clemente/quic-go/h2quic)
# https://github.com/caddyserver/caddy/commit/0b2e054
# https://github.com/mholt/certmagic/commit/6a42ef9
BuildRequires:  golang(github.com/mholt/certmagic) >= 0.6.2
BuildRequires:  golang(github.com/naoina/toml)
BuildRequires:  golang(gopkg.in/russross/blackfriday.v1)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(gopkg.in/mcuadros/go-syslog.v2)
BuildRequires:  golang(gopkg.in/mcuadros/go-syslog.v2/format)
%endif

# http plugins
%if %{with geoip}
BuildRequires:  golang(github.com/aablinov/caddy-geoip)
%endif
%if %{with realip}
BuildRequires:  golang(github.com/captncraig/caddy-realip)
%endif

# dns plugins
%if %{with azure}
BuildRequires:  golang(github.com/caddyserver/dnsproviders/azure)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/azure)
%endif
%if %{with cloudflare}
BuildRequires:  golang(github.com/caddyserver/dnsproviders/cloudflare)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/cloudflare)
%endif
%if %{with digitalocean}
BuildRequires:  golang(github.com/caddyserver/dnsproviders/digitalocean)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/digitalocean)
%endif
%if %{with googlecloud}
BuildRequires:  golang(github.com/caddyserver/dnsproviders/googlecloud)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/gcloud)
%endif
%if %{with pdns}
BuildRequires:  golang(github.com/caddyserver/dnsproviders/pdns)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/pdns)
%endif
%if %{with rackspace}
BuildRequires:  golang(github.com/caddyserver/dnsproviders/rackspace)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/rackspace)
%endif
%if %{with route53}
BuildRequires:  golang(github.com/caddyserver/dnsproviders/route53)
BuildRequires:  golang(github.com/go-acme/lego/providers/dns/route53)
%endif

BuildRequires:  systemd
%{?systemd_requires}

Provides:       webserver


%description %{common_description}

This package was built with the following plugins:

%{?with_geoip:  http.geoip
}%{?with_realip:  http.realip
}%{?with_azure:  tls.dns.azure
}%{?with_cloudflare:  tls.dns.cloudflare
}%{?with_digitalocean:  tls.dns.digitalocean
}%{?with_googlecloud:  tls.dns.googlecloud
}%{?with_pdns:  tls.dns.powerdns
}%{?with_rackspace:  tls.dns.rackspace
}%{?with_route53:  tls.dns.route53
}


%gopkg


%prep
%goprep
%patch0 -p 1
%patch1 -p 1

sed                     -e '/where other plugins get plugged in/ a \\t// plugins added during rpmbuild' \
%{?with_geoip:          -e '/where other plugins get plugged in/ a \\t_ "github.com/aablinov/caddy-geoip"'} \
%{?with_realip:         -e '/where other plugins get plugged in/ a \\t_ "github.com/captncraig/caddy-realip"'} \
%{?with_azure:          -e '/where other plugins get plugged in/ a \\t_ "github.com/caddyserver/dnsproviders/azure"'} \
%{?with_cloudflare:     -e '/where other plugins get plugged in/ a \\t_ "github.com/caddyserver/dnsproviders/cloudflare"'} \
%{?with_digitalocean:   -e '/where other plugins get plugged in/ a \\t_ "github.com/caddyserver/dnsproviders/digitalocean"'} \
%{?with_googlecloud:    -e '/where other plugins get plugged in/ a \\t_ "github.com/caddyserver/dnsproviders/googlecloud"'} \
%{?with_pdns:           -e '/where other plugins get plugged in/ a \\t_ "github.com/caddyserver/dnsproviders/pdns"'} \
%{?with_rackspace:      -e '/where other plugins get plugged in/ a \\t_ "github.com/caddyserver/dnsproviders/rackspace"'} \
%{?with_route53:        -e '/where other plugins get plugged in/ a \\t_ "github.com/caddyserver/dnsproviders/route53"'} \
                        -i caddy/caddymain/run.go


%build
export LDFLAGS="${LDFLAGS:-} -X %{goipath}/caddy/caddymain.appVersion=v%{version} "
%gobuild -o %{gobuilddir}/bin/caddy %{goipath}/caddy


%install
%gopkginstall
install -D -m 0755 %{gobuilddir}/bin/caddy %{buildroot}%{_bindir}/caddy
install -D -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/caddy/caddy.conf
install -D -m 0644 %{S:2} %{buildroot}%{_unitdir}/caddy.service
install -D -m 0644 %{S:3} %{buildroot}%{_datadir}/caddy/index.html
install -d -m 0755 %{buildroot}%{_sysconfdir}/caddy/conf.d
install -d -m 0750 %{buildroot}%{_sharedstatedir}/caddy


%if %{with check}
%check
%gocheck
%endif


%pre
getent group caddy &> /dev/null || \
groupadd -r caddy &> /dev/null
getent passwd caddy &> /dev/null || \
useradd -r -g caddy -d %{_sharedstatedir}/caddy -s /sbin/nologin -c 'Caddy web server' caddy &> /dev/null
exit 0


%post
%systemd_post caddy.service

if [ -x /usr/sbin/getsebool ]; then
    # connect to ACME endpoint to request certificates
    setsebool -P httpd_can_network_connect on
fi
if [ -x /usr/sbin/semanage -a -x /usr/sbin/restorecon ]; then
    # file contexts
    semanage fcontext --add --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
    semanage fcontext --add --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
    semanage fcontext --add --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
    semanage fcontext --add --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
    restorecon -r %{_bindir}/caddy %{_datadir}/caddy %{_sysconfdir}/caddy %{_sharedstatedir}/caddy || :
fi
if [ -x /usr/sbin/semanage ]; then
    # QUIC
    semanage port --add --type http_port_t --proto udp 80   2> /dev/null || :
    semanage port --add --type http_port_t --proto udp 443  2> /dev/null || :
    # HTTP challenge alternate port
    semanage port --add --type http_port_t --proto tcp 5033 2> /dev/null || :
fi


%preun
%systemd_preun caddy.service


%postun
%systemd_postun_with_restart caddy.service

if [ $1 -eq 0 ]; then
    if [ -x /usr/sbin/getsebool ]; then
        # connect to ACME endpoint to request certificates
        setsebool -P httpd_can_network_connect off
    fi
    if [ -x /usr/sbin/semanage ]; then
        # file contexts
        semanage fcontext --delete --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
        semanage fcontext --delete --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
        semanage fcontext --delete --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
        semanage fcontext --delete --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
        # QUIC
        semanage port     --delete --type http_port_t --proto udp 80   2> /dev/null || :
        semanage port     --delete --type http_port_t --proto udp 443  2> /dev/null || :
        # HTTP challenge alternate port
        semanage port     --delete --type http_port_t --proto tcp 5033 2> /dev/null || :
    fi
fi


%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/caddy
%{_datadir}/caddy
%{_unitdir}/caddy.service
%dir %{_sysconfdir}/caddy
%dir %{_sysconfdir}/caddy/conf.d
%config(noreplace) %{_sysconfdir}/caddy/caddy.conf
%attr(0750,caddy,caddy) %dir %{_sharedstatedir}/caddy


%gopkgfiles


%changelog
* Mon Feb 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-3
- Rebuilt for GHSA-jf24-p9p9-4rjh

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 07 2019 Carl George <carl@george.computer> - 1.0.3-1
- Latest upstream
- Remove bundled lego and plugins
- Remove dyn, gandi, namecheap, and rfc2136 dns providers
- Add patch0 to fix `-version` flag
- Add patch1 to adjust blackfriday import path
- Add devel subpackages
- Run test suite

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Carl George <carl@george.computer> - 0.11.4-2
- Switch unit file from ProtectSystem strict to full rhbz#1706651

* Wed Mar 06 2019 Carl George <carl@george.computer> - 0.11.4-1
- Latest upstream
- Update bundled dnsproviders to 0.1.3
- Update bundled lego to 2.2.0
- Enable googlecloud, route53, and azure dns providers on epel7
- Allow custom http port with default config file rhbz#1685446

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Carl George <carl@george.computer> - 0.11.1-2
- Buildrequires at least golang 1.10

* Tue Nov 13 2018 Carl George <carl@george.computer> - 0.11.1-1
- Latest upstream
- Update bundled geoip

* Fri Oct 19 2018 Carl George <carl@george.computer> - 0.11.0-3
- Enable httpd_can_network_connect selinux boolean to connect to ACME endpoint rhbz#1641158
- Define UDP 80/443 as selinux http_port_t for QUIC rhbz#1608548
- Define TCP 5033 as selinux http_port_t for HTTP challenge rhbz#1641160

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Carl George <carl@george.computer> - 0.11.0-1
- Latest upstream

* Sat Apr 21 2018 Carl George <carl@george.computer> - 0.10.14-1
- Latest upstream
- Overhaul %%prep to extract everything with %%setup
- Edit lego providers to require acmev2 instead of acme
- Add provides for specific providers from %%import_path_dnsproviders and %%import_path_lego
- Add azure dns provider on f28+

* Fri Apr 20 2018 Carl George <carl@george.computer> - 0.10.11-6
- Enable geoip plugin on EL7
- Only provide bundled geoip/realip/dnsproviders/lego when the respective plugin is enabled

* Wed Apr 18 2018 Carl George <carl@george.computer> - 0.10.11-5
- Add geoip plugin

* Tue Apr 17 2018 Carl George <carl@george.computer> - 0.10.11-4
- Correct ExclusiveArch fallback

* Mon Apr 16 2018 Carl George <carl@george.computer> - 0.10.11-3
- Enable s390x
- Disable googlecloud and route53 dns providers on EL7 due to dependency issues

* Fri Mar 30 2018 Carl George <carl@george.computer> - 0.10.11-2
- Add googlecloud dns provider
- Add route53 dns provider
- Set minimum golang version to 1.9
- Set selinux labels in scriptlets

* Sat Feb 24 2018 Carl George <carl@george.computer> - 0.10.11-1
- Latest upstream

* Sat Feb 24 2018 Carl George <carl@george.computer> - 0.10.10-4
- Change ProtectSystem from strict to full in unit file on RHEL

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Carl George <carl@george.computer> - 0.10.10-2
- Add powerdns provider

* Mon Oct 09 2017 Carl George <carl@george.computer> - 0.10.10-1
- Latest upstream

* Mon Oct 02 2017 Carl George <carl@george.computer> - 0.10.9-6
- Add provides for bundled libraries

* Mon Oct 02 2017 Carl George <carl@george.computer> - 0.10.9-5
- Enable rfc2136 dns provider
- List plugins in description

* Mon Sep 18 2017 Carl George <carl@george.computer> - 0.10.9-4
- Exclude s390x

* Sun Sep 17 2017 Carl George <carl@george.computer> - 0.10.9-3
- Add realip plugin
- Add conditionals for plugins

* Sat Sep 16 2017 Carl George <carl@george.computer> - 0.10.9-2
- Add sources for caddyserver/dnsproviders and xenolf/lego
- Disable all dns providers that require additional libraries (dnsimple, dnspod, googlecloud, linode, ovh, route53, vultr)
- Rewrite default index.html

* Tue Sep 12 2017 Carl George <carl@george.computer> - 0.10.9-1
- Latest upstream
- Add config validation to unit file
- Disable exoscale dns provider https://github.com/xenolf/lego/issues/429

* Fri Sep 08 2017 Carl George <carl@george.computer> - 0.10.8-1
- Latest upstream
- Build with %%gobuild macro
- Move config subdirectory from /etc/caddy/caddy.conf.d to /etc/caddy/conf.d

* Tue Aug 29 2017 Carl George <carl@george.computer> - 0.10.7-1
- Latest upstream

* Fri Aug 25 2017 Carl George <carl@george.computer> - 0.10.6-2
- Use SIQQUIT to stop service
- Increase the process limit from 64 to 512
- Only `go get` in caddy/caddymain

* Fri Aug 11 2017 Carl George <carl@george.computer> - 0.10.6-1
- Latest upstream
- Add webserver virtual provides
- Drop tmpfiles and just own /var/lib/caddy directly
- Remove PrivateDevices setting from unit file, it prevents selinux process transitions
- Disable rfc2136 dns provider https://github.com/caddyserver/dnsproviders/issues/11

* Sat Jun 03 2017 Carl George <carl.george@rackspace.com> - 0.10.3-2
- Rename Envfile to envfile
- Rename Caddyfile to caddy.conf
- Include additional configs from caddy.conf.d directory

* Fri May 19 2017 Carl George <carl.george@rackspace.com> - 0.10.3-1
- Latest upstream

* Mon May 15 2017 Carl George <carl.george@rackspace.com> - 0.10.2-1
- Initial package
