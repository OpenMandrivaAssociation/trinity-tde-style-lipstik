%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tde-style-lipstik
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	2.2.3
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Lipstik style for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/themes/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

Obsoletes:		trinity-kde-style-lipstik < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kde-style-lipstik = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-style-lipstik < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-style-lipstik = %{?epoch:%{epoch}:}%{version}-%{release}

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Based on the plastik style, Lipstik is a purified style with many options to
tune your desktop look.

Lipstik also provides Lipstik-color-schemes


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/%{_lib}/trinity/tdestyle_lipstik_config.la
%{tde_prefix}/%{_lib}/trinity/tdestyle_lipstik_config.so
%{tde_prefix}/%{_lib}/trinity/plugins/styles/lipstik.la
%{tde_prefix}/%{_lib}/trinity/plugins/styles/lipstik.so
%{tde_prefix}/share/apps/tdedisplay/color-schemes/lipstiknoble.kcsrc
%{tde_prefix}/share/apps/tdedisplay/color-schemes/lipstikstandard.kcsrc
%{tde_prefix}/share/apps/tdedisplay/color-schemes/lipstikwhite.kcsrc
%{tde_prefix}/share/apps/tdestyle/themes/lipstik.themerc

